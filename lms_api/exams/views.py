from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404

from .models import Question


def index(request):
    questions = Question.objects.order_by("-id")
    data = []
    for question in questions:
        data.append({
            'text': question.text
        })

    return JsonResponse(data, safe=False)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    data = {
        'text': question.text
    }

    return JsonResponse(data, safe=False)


def choices(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    data = []
    for choice in question.choice_set.all():
        data.append({
            'text': choice.text
        })

    #raise Exception("I want to know the value of this: " + str(data))
    return JsonResponse(data, safe=False)
