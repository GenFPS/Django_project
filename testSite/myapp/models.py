from django.db import models


# Создаем класс Product для таблицы Product в бд Sqlite3
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=200)

    # Вместо product object будет выдавать название по полю name таблицы Product
    def __str__(self) -> models.CharField:
        return self.name
