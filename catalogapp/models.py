from django.db import models


# Тип категории - например "Расход"
class CategoryType(models.Model):
    name = models.CharField(max_length=32, verbose_name='Тип категории')

    def __str__(self):
        return self.name


# Категория - например "Автомобиль"
class Category(models.Model):
    category_type = models.ForeignKey(CategoryType, on_delete=models.CASCADE, verbose_name='Тип категории')
    name = models.CharField(max_length=64, verbose_name='Название категории')

    def __str__(self):
        return self.name


# Расход или доход из категории - например "Бензин"
class CategoryUnit(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=128, verbose_name='Название')

    def __str__(self):
        return self.name
