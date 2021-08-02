from rest_framework import serializers
from .models import *

class QuizSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Quiz
        fields = [
            'title',
            'start_time',
            'end_time',
        ]

class AnswerSerializer(serializers.ModelSerializer):
    # question = QuestionSerializer(read_only=True)

    class Meta:
        model = Answer
        fields = [
            # 'question',
            'id',
            'answer_text',
            'is_right',
        ]

class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = [
            'id',
            'title',
            'img',
            'answer',
        ]