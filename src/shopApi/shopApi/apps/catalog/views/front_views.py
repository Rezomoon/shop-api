from rest_framework import viewsets
from shopApi.apps.catalog.models import Category
from shopApi.apps.catalog.serializers.front_ser import CategorySerializer , FrontCategoryTreesSerializer
class CategoryViewSet(viewsets.ReadOnlyModelViewSet) :
   
    queryset            = Category.objects.public()
    serializer_class    = FrontCategoryTreesSerializer

    # def get_queryset(self):
    #     return Category.objects.filter(is_public=True)
   