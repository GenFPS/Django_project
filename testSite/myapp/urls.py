from django.urls import path
from myapp import views

app_name = 'myapp'

urlpatterns = [
    # http://127.0.0.1:8000/myapp/items/
    path('', views.items),

    # http://127.0.0.1:8000/myapp/items/<my_id>/
    path('items_<int:my_id>/', views.details_id, name='item')     # 3-ий параметр - позволяет гибко
    # изменять название пути до страниц (в index.html: <a href="{% url 'detailItem' item.id %}">)
]
