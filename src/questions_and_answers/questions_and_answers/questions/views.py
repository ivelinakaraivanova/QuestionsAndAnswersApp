from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from questions_and_answers.questions.forms import UserRegistrationForm, QuestionRegistrationForm, AnswerForm, \
    QuestionUpdateForm, AnswerUpdateForm, ProfileForm
from questions_and_answers.questions.models import Question, Answer


def questions_list(request):

    if 'q' in request.GET:
        q = request.GET['q']
        questions = Question.objects.filter(title__icontains=q).order_by('-created_at')
    else:
        questions = Question.objects.all().order_by('-created_at')

    context = {
        'questions': questions
    }

    return render(request, 'qa_list.html', context)


@login_required
def question_details(request, slug):
    question = get_object_or_404(Question, slug=slug)
    answers = Answer.objects.filter(question=question)

    if request.method == "POST":
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            answer = answer_form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer = answer_form.save()
            return redirect('question_details', slug=question.slug)
    else:
        answer_form = AnswerForm()

    context = {
        'question': question,
        'answers': answers,
        'answer_form': answer_form
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


@login_required
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


@login_required
def update_question(request, slug):
    question = get_object_or_404(Question, slug=slug)

    form = QuestionUpdateForm(request.POST or None, instance=question)
    if form.is_valid():
        form.save()
        return redirect('questions_list')

    context = {
        'form': form
    }

    return render(request, 'update_question.html', context)


@login_required
def delete_question(request, slug):
    question = get_object_or_404(Question, slug=slug)
    question.delete()
    return redirect('questions_list')


@login_required
def update_answer(request, id):
    answer = get_object_or_404(Answer, id=id)

    form = AnswerUpdateForm(request.POST or None, instance=answer)
    if form.is_valid():
        form.save()
        return redirect('question_details', slug=answer.question.slug)

    context = {
        'form': form
    }

    return render(request, 'update_answer.html', context)


@login_required
def delete_answer(request, id):
    answer = get_object_or_404(Answer, id=id)
    answer.delete()
    return redirect('question_details', slug=answer.question.slug)


@login_required
def change_profile(request):
    if request.method == "POST":
        profile_form = ProfileForm(request.POST, instance=request.user)

        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile has been changed successfully')

    profile_form = ProfileForm(instance=request.user)

    return render(request, 'registration/profile.html', {'profile_form': profile_form})


@login_required
def list_info(request):
    questions = Question.objects.filter(author=request.user).order_by('-created_at')
    answers = Answer.objects.filter(author=request.user).order_by('-created_at')

    context = {
        'questions': questions,
        'answers': answers
    }

    return render(request, 'list_info.html', context)