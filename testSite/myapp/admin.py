from django.contrib import admin

from .models import Product

# Регистрируем таблицу Product
admin.site.register(Product)
