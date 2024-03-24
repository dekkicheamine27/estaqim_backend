from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Student
from firebase_admin import auth, exceptions
from .serializers import StudentDetailSerializer, StudentOrderSerializer
from radio_estaqim import settings
from quizzes.models import QuizScore
from django.db.models import Sum
from django.db.models import Window, F
from django.db.models.functions import Rank

User = get_user_model()

class TopStudentsAPIView(APIView):
    def get(self, request):
        # Get the top 10 students ordered by score
        students_with_rank = Student.objects.annotate(
            rank=Window(
                expression=Rank(),
                order_by=[F('score').desc(), F('course').desc()]
            )
        )

        # Fetch the top 20 students.
        top_students = students_with_rank.order_by('rank')[:10]

        # Serialize the queryset
        serializer = StudentOrderSerializer(top_students, many=True)

        # Return the serialized data
        return Response(serializer.data)

def update_student_score(student):
    total_score = QuizScore.objects.filter(student=student).aggregate(total_score=Sum('score'))['total_score'] or 0
    student.score = total_score
    student.save()
    return student

def get_student_rank(student):
    # Count the number of students with a higher score to determine the rank.
    # This approach assumes that a higher score results in a better rank.
    higher_score_count = Student.objects.filter(score__gt=student.score).count()
    return higher_score_count + 1

class StudentDetailView(APIView):
    def get(self, request, *args, **kwargs):
        # Extract the Firebase ID token from the Authorization header
        token = request.headers.get('Authorization', '').split('Bearer ')[-1].strip()


        if not token:
            return Response({'error': 'Authorization token required'}, status=status.HTTP_401_UNAUTHORIZED)

        try:

            # Verify the Firebase ID token and extract user information
            decoded_token = auth.verify_id_token(token)
            firebase_uid = decoded_token['uid']
            # Extract name from the decoded token
            name = decoded_token.get('name', 'Default Name')
            email = decoded_token.get('email',)


            # Ensure a StudentDetail object exists for the user, including setting the name from Firebase
            student_detail, created = Student.objects.get_or_create(
                firebase_uid=firebase_uid,
                defaults={'name': name, 'email': email }
            )
            student_detail = update_student_score(student_detail)
            # Prepare and return the response data
            rank = get_student_rank(student_detail)

            data = {
                'id': student_detail.id,
                'rank': rank,
                'name': student_detail.name,
                'email': student_detail.email,
                'city': student_detail.city,
                'country': student_detail.country,
                'birthday':student_detail.birthday,
                'level': student_detail.level,
                'book': student_detail.book,
                'course': student_detail.course,
                'mosabaka': student_detail.mosabaka,
                'score': student_detail.score,
                'created': created
            }
            return Response(data, status=status.HTTP_200_OK)


        except exceptions.FirebaseError as e:
            return Response({'error': str(e)}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def patch(self, request, *args, **kwargs):
        token = request.headers.get('Authorization', '').split('Bearer ')[-1].strip()

        if not token:
            return Response({'error': 'Authorization token required'}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            decoded_token = auth.verify_id_token(token)
            firebase_uid = decoded_token['uid']

            student_detail = Student.objects.get(firebase_uid=firebase_uid)
            student_detail = update_student_score(student_detail)

            rank = get_student_rank(student_detail)
            student_detail.rank = rank
            # Use the serializer for updating student details
            serializer = StudentDetailSerializer(student_detail, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()

                # Return the updated student details
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        except exceptions.FirebaseError:
            return Response({'error': 'Invalid Firebase ID token'}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
