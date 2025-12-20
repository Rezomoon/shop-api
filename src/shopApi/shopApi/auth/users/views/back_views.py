from rest_framework.authtoken.views import ObtainAuthToken
from shopApi.auth.users.serializer.back_ser import AdminLoginAuthSerializer
class AdminLoginView(ObtainAuthToken) : 
    serializer_class = AdminLoginAuthSerializer