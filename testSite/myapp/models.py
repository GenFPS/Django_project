from django.db.models import Model, CharField, IntegerField


# Создаем класс Product для таблицы Product в бд Sqlite3
class Product(Model):
    name = CharField(max_length=100)
    price = IntegerField()
    description = CharField(max_length=200)

    # Вместо product object будет выдавать название по полю name таблицы Product (история добавления товаров
    # в панеле admin)
    def __str__(self) -> CharField:
        return self.name
