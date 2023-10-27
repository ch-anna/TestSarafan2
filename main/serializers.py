from rest_framework.serializers import ModelSerializer
from .models import Category, SubCategory, Item

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubCategorySerializer(ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'