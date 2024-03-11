from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    # http://127.0.0.1:8000/admin/
    path('admin/', admin.site.urls),
    # http://127.0.0.1:8000/greeting/
    path('greeting/', views.response),
    # http://127.0.0.1:8000/contacts/
    path('contacts/', views.contacts),
    # http://127.0.0.1:8000/items/
    path('items/', views.items)
]
