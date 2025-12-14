from  rest_framework import serializers
from shopApi.apps.catalog.models import Category
from rest_framework.generics import get_object_or_404
#
class CreateCategoryNodeSerializer(serializers.ModelSerializer) :
    # chon k mikhayeem bebinim k aya in category vared shode zir majmoe va chilz yek data dige hast ya na
    # va ya inke b onvane parent hast bayad b yek sorat motevajeh beshim inja yek data va field joda gane migirim 
    # masalan b esme parent 
    parent  = serializers.IntegerField(
        write_only  = True ,# WRITE_ONLY : Agar k bekhahim az in serializer ham read konim va ham write va chon dar dataBase in feild vojod nadarad
        # bedone write only data Sakhteh mishavad ama neshanesh nimde !va ba write_only in moshkel hal mishavad !
    
        required    = False , # ejaze mideh etelat bedone field parent ersal shavand
        allow_null  = True    # ejaze mideh k agar field bod khali bashad 
    )
    # inja ham bayad b onvane yek int tarifesh chera k id ha dar DB ma int hastand
    # va agar k khali bood khode data b onvane yek parent save mishe va age por bashe bayad int id yek data dige ro bede a childesh beshe !


    # Chod Serialzier ma mikhad yek data besaze b method create niaz darim va in method bad az 
    # valid shodan ha ejra mishavad !
    def create(self , validated_data) :
        parent  = validated_data.pop("parent" , None)
        if parent is None :
            instance    = Category.add_root(**validated_data)
        else : 
            parent_node = get_object_or_404(Category , pk=parent)
            instance    = parent_node.add_child(**validated_data)
        return instance
    class Meta : 
        model   = Category
        fields  = ("title" , "describtion" , "is_public" , "slug" ,"parent")
        # exclude = 

class CategorytreeSerializer(serializers.ModelSerializer) : 
    # baraye derakhti neshan dadane data ha bayad yek field ezafeh kard =>(children)
    # 2 ta halat dare inja ya bayad khodemoon berim az ghabl besazimesh va b shekl dreakhti bargardonimesh
    # ya inke chon darim az MP_Node estefadeh mikonim khodesh yek method get_children behemoon mideh 
    # va in roo mishe b shekle bazgashti estefadeh kard
    children    = serializers.SerializerMethodField()
    #   in royekard kheyli behine nist 
    def get_children(self , obj):
        # chon serilizer moethon field hastesh bayad yek get_children dashteh bashim
        return CategorytreeSerializer(obj.get_children() , many = True).data # in get_children() inja baraye methode MP_Node hastesh
    class Meta : 
        model   = Category 
        fields  = ("title" , "describtion" , "is_public" , "slug" ,"children")

class CategoryNodeTreeSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = Category
        fields = "__all__"