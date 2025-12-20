from rest_framework.routers import SimpleRouter
from django.urls import path
from shopApi.auth.users.views.back_views import AdminLoginView
# # #
router = SimpleRouter()
urlpatterns = [
    path('api-token-auth/', AdminLoginView.as_view()) , 
] + router.urls  