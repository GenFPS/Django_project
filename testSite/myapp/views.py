from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def response(request) -> HttpResponse:
    return HttpResponse('Here\'s your response\n'
                        '\nGlad to see you here! =)')


def contacts(request) -> HttpResponse:
    return HttpResponse('<h1>Наши контакты</h1>')

def items(requests) -> HttpResponse:
    items = ['Iphone', 'Samsung', 'Huawie']
    return HttpResponse(items[0])
