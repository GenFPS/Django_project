from django.shortcuts import render     # для рендеринга шаблона html-страницы
from django.http import HttpResponse
from .models import Product


# Create your views here.
def response(request) -> HttpResponse:
    return HttpResponse(f'Here\'s your response\n'
                        f'\nGlad to see you here! =)')


def items(requests) -> render:
    items = Product.objects.all()
    context = {
        'items': items
    }
    return render(request=requests, template_name='myapp/index.html', context=context)


# Рендеринг myapps/details.html - обращение по id к товару
def details_id(request, my_id: int) -> render:
    # Используем поле id из таблицы данных Product
    item = Product.objects.get(id=my_id)
    context = {
        'item': item
    }
    return render(request=request, template_name='myapp/details.html', context=context)
