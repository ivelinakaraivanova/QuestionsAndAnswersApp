from django.shortcuts import render, get_object_or_404

from questions_and_answers.questions.models import Question


def questions_list(request):
    questions = Question.objects.all().order_by('-created_at')

    context = {
        'questions': questions
    }

    return render(request, 'qa_list.html', context)


def question_details(request, slug):
    question = get_object_or_404(Question, slug=slug)

    context = {
        'question': question
    }

    return render(request, 'q_details.html', context)
