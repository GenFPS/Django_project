from django.urls import path
from myapp import views

urlpatterns = [
    # http://127.0.0.1:8000/myapp/greeting/
    path('greeting/', views.response),

    # http://127.0.0.1:8000/myapp/contacts/
    path('contacts/', views.contacts),

    # http://127.0.0.1:8000/myapp/items/
    path('items/', views.items),

    # http://127.0.0.1:8000/myapp/items/<my_id>/
    path('items/<int:my_id>/', views.details_id, name='detailItem')     # 3-ий параметр - позволяет гибко
    # изменять название пути до страниц (в index.html: <a href="{% url 'detailItem' item.id %}">)
]