from rest_framework import viewsets
from shopApi.apps.catalog.models import Category
from shopApi.apps.catalog.serializers.back_ser import CreateCategoryNodeSerializer ,CategorytreeSerializer , CategoryNodeTreeSerializer , CategoryModificationSerializer
# 
class CategoryViewSet(viewsets.ModelViewSet) : 
    queryset     = Category.objects.all()
    serializer_class    = CreateCategoryNodeSerializer


    def get_queryset(self):
        if self.action == "list" : 
            return Category.objects.filter(depth = 1)
        else : 
            return Category.objects.all()
        
        return super().get_queryset()
    def get_serializer_class(self):
        # In baraye ine k agar darkhaste get dashtim data haro ba serialzer mojaza neshan bedeh
        if self.action == "list"        :
            return CategorytreeSerializer
        elif self.action == "create"    :
            return CreateCategoryNodeSerializer
        elif self.action == "retrieve"  :
            return CategoryNodeTreeSerializer
        elif self.action == "update"    :   
            return CategoryModificationSerializer
        elif self.action == "partial_update" : # in asamie dakhele "" dar Viewset set shodan 
            return CategoryModificationSerializer
        elif self.action == "destroy"   : 
            return CategoryModificationSerializer


# Dar vaghe ma bayad va mitonestim az match pattern estefadeh konim ama py v balaye 3.10 mikhad 
        # match self.action :
        #     case "list" :
        #         return CategorytreeSerializer
        #     case "create" :
        #         return CreateCategoryNodeSerializer
        #     case  _ ""
            
        
        return super().get_serializer_class()