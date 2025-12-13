from rest_framework.routers import SimpleRouter
from shopApi.apps.catalog.views.front_views import CategoryViewSet

# # #
router = SimpleRouter()
router.register('categories' , CategoryViewSet , basename="Catagory") # Baraye Viewset hayee k get hastand momkene k get_query set nadashte bashand pas banabar in bayad baseName ro ezafeh kard
urlpatterns = [] + router.urls  