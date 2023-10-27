from rest_framework.routers import SimpleRouter
from .views import CategoryPage, SubCategoryPage, ItemsPage

router = SimpleRouter()
router.register('api/category', CategoryPage)
router.register('api/subcategory', SubCategoryPage)
router.register('api/items', ItemsPage)

urlpatterns = []
urlpatterns += router.urls