from django.shortcuts import render, get_object_or_404, redirect

from questions_and_answers.questions.forms import UserRegistrationForm, QuestionRegistrationForm
from questions_and_answers.questions.models import Question, Answer


def questions_list(request):
    questions = Question.objects.all().order_by('-created_at')

    context = {
        'questions': questions
    }

    return render(request, 'qa_list.html', context)


def question_details(request, slug):
    question = get_object_or_404(Question, slug=slug)
    answers = Answer.objects.filter(question=question)

    context = {
        'question': question,
        'answers': answers
    }

    return render(request, 'q_details.html', context)


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'register_done.html', {'user_form': user_form})

    else:
        user_form = UserRegistrationForm()

    return render(request, 'register.html', {'user_form': user_form})


def add_question(request):

    if request.method == "POST":
        question_form = QuestionRegistrationForm(request.POST)

        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.author = request.user
            question = question_form.save()

            return redirect('questions_list')

    else:
        question_form = QuestionRegistrationForm()

    return render(request, 'add_question.html', {'question_form': question_form})

