from django.shortcuts import render     # для рендеринга шаблона html-страницы
from django.http import HttpResponse
from .models import Product


# Create your views here.
def response(request) -> HttpResponse:
    return HttpResponse('Here\'s your response\n'
                        '\nGlad to see you here! =)')


def contacts(request) -> HttpResponse:
    return render(request=request, template_name='myapp/contact.html')  # указываем путь до contact.html


def items(requests) -> HttpResponse:
    items = Product.objects.all()
    return HttpResponse(items)
