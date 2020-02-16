from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World")


def detail(request, question_id):
    return HttpResponse("Your looking at question {}".format(question_id))

def results(request, question_id):
    return HttpResponse("Your looking at the results of question {}".format(question_id))

def vote(request, question_id):
    return HttpResponse("You're voting on question {}".format(question_id))




