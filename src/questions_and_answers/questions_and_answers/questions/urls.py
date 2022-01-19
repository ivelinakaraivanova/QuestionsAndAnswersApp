from django.urls import path

from questions_and_answers.questions.views import questions_list, question_details

urlpatterns = [
    path('questions/', questions_list, name='questions_list'),
    path('questions/<slug:slug>', question_details, name='question_details'),
]