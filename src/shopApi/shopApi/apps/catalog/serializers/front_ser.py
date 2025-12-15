from rest_framework import serializers
from shopApi.apps.catalog.models import Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta : 

        model = Category

        fields  ='__all__' #  inke ch feild hayeero mikhayeem baramoon bargardoone 