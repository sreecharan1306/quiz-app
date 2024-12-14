from django.db import models

import random

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=1)  # 'A', 'B', 'C', or 'D'

    def __str__(self):
        return self.question_text

class QuizSession(models.Model):
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)

class UserAnswer(models.Model):
    quiz_session = models.ForeignKey(QuizSession, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answer = models.CharField(max_length=1)  # 'A', 'B', 'C', or 'D'
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.quiz_session.id} - {self.question.question_text} - {self.selected_answer}"