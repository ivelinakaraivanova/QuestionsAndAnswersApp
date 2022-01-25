from django import forms
from django.contrib.auth import get_user_model

from questions_and_answers.questions.models import Question, Answer

User = get_user_model()


class UserRegistrationForm(forms.ModelForm):

    password = forms.CharField(
        label='Password',
        widget= forms.PasswordInput,
    )

    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        clean_data = self.cleaned_data
        if clean_data['password'] != clean_data['password2']:
            raise forms.ValidationError("Passwords don't match")

        return clean_data['password2']


class QuestionRegistrationForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'body')


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('description',)


class QuestionUpdateForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'body')


class AnswerUpdateForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('description',)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
