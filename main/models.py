from django.db import models

# Create your models here.

class Category(models.Model):
    slug = models.SlugField('Уникальное название категории', unique=True)
    title = models.CharField('Название категории', max_length=120)
    image = models.ImageField('Изображение категории', upload_to='pictures/category')

    def __str__(self):
        return self.title

class SubCategory(models.Model):
    slug = models.SlugField('Уникальное название подкатегории', unique=True)
    title = models.CharField('Название подкатегории', max_length=120)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    image = models.ImageField('Изображение подкатегории', upload_to='pictures/subcategory')

    def __str__(self):
        return self.title


class Item(models.Model):
    slug = models.SlugField('Уникальное название продукта', unique=True)
    title = models.CharField('Название продукта', max_length=120)
    img = models.ImageField('Изображение продукта', upload_to='pictures/items')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Цена')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name='Подкатегория продукта')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория продукта')

    def __str__(self):
        return self.title