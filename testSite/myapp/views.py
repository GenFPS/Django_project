from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def response(request: str) -> HttpResponse:
    return HttpResponse('Here\'s your response\n'
                        '\nGlad to see you here! =)')


def contacts(request: str) -> HttpResponse:
    return HttpResponse('<h1>Наши контакты</h1>')
