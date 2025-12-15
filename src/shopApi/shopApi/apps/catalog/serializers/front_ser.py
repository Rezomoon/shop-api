from rest_framework import serializers
from shopApi.apps.catalog.models import Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta : 

        model = Category

        fields  ='__all__' #  inke ch feild hayeero mikhayeem baramoon bargardoone 

class FrontCategoryTreesSerializer(serializers.ModelSerializer) :
    # Show Data In Tree GraphgQl
    
    children    = serializers.SerializerMethodField()

    def get_children(self,obj):
        return FrontCategoryTreesSerializer(obj.get_children() , many = True).data
    
    class Meta : 
        model   = Category
        fields  = ("title" , "describtion" ,"is_public" , "slug" ,"children" )
