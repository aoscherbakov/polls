from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Question

def index(request):
    lat_quest_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.quest_text for q in lat_quest_list])

    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse("Your looking at question {}".format(question_id))

def results(request, question_id):
    return HttpResponse("Your looking at the results of question {}".format(question_id))

def vote(request, question_id):
    return HttpResponse("You're voting on question {}".format(question_id))




