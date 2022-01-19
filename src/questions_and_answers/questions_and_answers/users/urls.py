from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from questions_and_answers.questions.views import register

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', register, name='register'),
]