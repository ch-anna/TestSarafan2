from django.contrib import admin
from .models import Category
from .models import SubCategory
from .models import Item

# Register your models here.

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Item)