from django.urls import path

from questions_and_answers.questions.views import questions_list, question_details, add_question

urlpatterns = [
    path('questions/', questions_list, name='questions_list'),
    path('questions/<slug:slug>', question_details, name='question_details'),
    path('questions/add/', add_question, name='add_question'),
]