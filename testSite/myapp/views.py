from django.shortcuts import render     # для рендеринга шаблона html-страницы
from django.http import HttpResponse
from .models import Product


# Create your views here.
def response(request) -> HttpResponse:
    return HttpResponse(f'Here\'s your response\n'
                        f'\nGlad to see you here! =)')


def contacts(request) -> render:
    return render(request=request, template_name='myapp/contact.html')  # указываем путь до contact.html


def items(requests) -> render:
    items = Product.objects.all()
    context = {
        'items': items
    }
    return render(request=requests, template_name='myapp/index.html', context=context)


def item_id(request, item_id: int) -> render:
    return HttpResponse(f'The item id is {item_id}')
