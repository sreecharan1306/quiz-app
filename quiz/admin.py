from django.contrib import admin
from .models import Question, QuizSession, UserAnswer

admin.site.register(Question)
admin.site.register(QuizSession)
admin.site.register(UserAnswer)

#super user
#username: mscha
#password: lc_profile