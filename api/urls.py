from django.urls import path
from .views import *

urlpatterns = [
    path('', LiveQuiz.as_view(), name='live'),
    path('p/', PastQuiz.as_view(), name='past'),
    path('f/', FutureQuiz.as_view(), name='future'),
    path('q/<str:topic>', QuizQuestion.as_view(), name='quiz'),
]