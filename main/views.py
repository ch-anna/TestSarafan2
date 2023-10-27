from .serializers import CategorySerializer, SubCategorySerializer, ItemSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Category, SubCategory, Item
from rest_framework.pagination import PageNumberPagination

# Create your views here.

class CategoryPagePagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10


class CategoryPage(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagePagination

class SubCategoryPage(ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

class ItemsPage(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer