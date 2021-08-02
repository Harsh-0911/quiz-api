from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

class LiveQuiz(APIView):
    def get(self, request, **kwargs):
        now = timezone.now()
        quiz = Quiz.objects.filter(start_time__lte=now,
        end_time__gte=now)
        serializer = QuizSerializer(quiz, many=True)
        return Response(serializer.data)

class PastQuiz(APIView):
    def get(self, request, **kwargs):
        now = timezone.now()
        quiz = Quiz.objects.filter(start_time__lte=now,
        end_time__lte=now)
        serializer = QuizSerializer(quiz, many=True)
        return Response(serializer.data)

class FutureQuiz(APIView):
    def get(self, request, **kwargs):
        now = timezone.now()
        quiz = Quiz.objects.filter(start_time__gte=now,
        end_time__gte=now)
        serializer = QuizSerializer(quiz, many=True)
        return Response(serializer.data)

class QuizQuestion(APIView):
    def get(self, request, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs['topic'])
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)

# class QuizAnswer(APIView):
#     def get(self, request, **kwargs):
#         answer = Answer.objects.filter(question__quiz__title=kwargs['topic'])
#         serializer = AnswerSerializer(answer, many=True)
#         return Response(serializer.data)
