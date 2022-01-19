from django.contrib import admin

from questions_and_answers.users.models import CustomUser

admin.site.register(CustomUser)