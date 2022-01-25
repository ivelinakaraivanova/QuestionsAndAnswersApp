from django.urls import path

from questions_and_answers.questions.views import questions_list, question_details, add_question, update_question, \
    delete_question, update_answer, delete_answer, change_profile, list_info

urlpatterns = [
    path('questions/', questions_list, name='questions_list'),
    path('questions/<slug:slug>', question_details, name='question_details'),
    path('questions/add/', add_question, name='add_question'),
    path('question/update/<slug:slug>/', update_question, name='update_question'),
    path('question/delete/<slug:slug>/', delete_question, name='delete_question'),
    path('answer/update/<int:id>/', update_answer, name='update_answer'),
    path('answer/delete/<int:id>/', delete_answer, name='delete_answer'),
    path('profile/', change_profile, name='change_profile'),
    path('list/', list_info, name='list_info')
]