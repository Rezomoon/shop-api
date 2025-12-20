from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

@admin.register(User)
class AdminUserShopApi(UserAdmin) : 
    list_display = ("username", "email", "first_name", "last_name", "is_staff" , "verified_email")