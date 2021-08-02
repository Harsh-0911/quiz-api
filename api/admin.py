from django.contrib import admin
from .models import *

class AnswerInlineModel(admin.TabularInline):
    model = Answer
    fields = [
        'answer_text',
        'is_right',
    ]

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    class Meta:
        model = Quiz
        fields = '__all__'
    
    list_display = [
        'id', 
        'title', 
        'start_time', 
        'end_time'
    ]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    class Meta:
        model = Question
        fields = '__all__'
    
    list_display = [
        'id', 
        'quiz', 
        'title', 
        'img'
    ]
    
    inlines = [
        AnswerInlineModel,
    ]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    class Meta:
        model = Answer
        fields = '__all__'

    list_display = [
        'answer_text',
        'is_right',
        'question',
    ]
