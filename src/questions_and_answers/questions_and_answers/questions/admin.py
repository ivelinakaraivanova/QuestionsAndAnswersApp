from django.contrib import admin

from questions_and_answers.questions.models import Question, Answer

admin.site.register(Question)
admin.site.register(Answer)
