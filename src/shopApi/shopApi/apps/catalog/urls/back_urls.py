from rest_framework.routers import SimpleRouter
from shopApi.apps.catalog.views.back_views import CategoryViewSet

# # #
router = SimpleRouter()
router.register('categories' , CategoryViewSet ,basename="CategoryshopApi/apps/catalog/serializers/back_ser.py") # Baraye Viewset hayee k get hastand momkene k get_query set nadashte bashand pas banabar in bayad baseName ro ezafeh kard
urlpatterns = [] + router.urls  