from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from .models import Category , ProductClass , Option , ProductAttribute , OptionGroup , Product

# Register your models here.


# In ro az khode package treebeard baraye edit django admin gerftim
class MyAdmin(TreeAdmin):
    form = movenodeform_factory(Category)

admin.site.register(Category, MyAdmin)




# Baraye ezafeh kardane va inke betavanim yek Table vabaste b yek Tabele digar ra hengame sakhtane yek data dar Tabele aval
# b data base ezafeh konim bayad dar Class AdminModel oon Tabeli k behesh fk mikhore  ghesmate inline ezafeh shavad !
# Va Bayad Baraye Table k field fk dar models oon vojod darad Bayad yek class Ba ers barai az class haye  admin.TabularInline va ya admin.StackedInline
# besazim !
# 1 >
class ProductAttributeAdminModelInLine(admin.TabularInline):  
    model       = ProductAttribute
    extra       = 2 # Chanta Bashe b Shekle Default
# 2 >
class ProductAttributeAdminModelStackedInline(admin.StackedInline) :
    model       = ProductAttribute
    extra       = 2
admin.site.register(ProductAttribute)



@admin.register(OptionGroup)
class OptionGroupModelAdmin(admin.ModelAdmin) : 
    list_display    = ["title" ]
    list_filter     = ["title" ]
    inlines         = [ProductAttributeAdminModelStackedInline] # Baraye Inke betavan hengam sakhte yek data az in table yek dat az Table vabaste b in table(fk) sakht

# admin.site.register(Option) 

@admin.register(ProductClass)
class ProductClassAdminModel(admin.ModelAdmin) :
    list_display    =   ("title" ,
                        "describtion" , 
                        "require_shipping",
                        "track_stock", 
                        "attribute_count") # Baraye Neshan Dadane Field Ha Dar List Dar DjangoAdmin
    

    list_filter     =   ("title" ,
                        "describtion" ,
                        "require_shipping",
                        "track_stock") # Baraye Filter kardane Field ha dar DjangoAdmin
    inlines         = [ProductAttributeAdminModelInLine ]  # Baraye Inke betavan hengam sakhte yek data az in table yek dat az Table vabaste b in table(fk) sakht


    def attribute_count(self , obj) :
        # Mishavad Ba in function va b in sorat yek seri custom attribute dorost kard !
        # Tip : attributes inja field Table Product nistesh va dar vaghe yek kelid khareji hast az table product attribute k related_name in field attributes zakhireh shode
        return obj.attributes.count()

    def enable_track_stock(self,request , queryset):
            queryset.update(track_stock = True)
    actions = ["enable_track_stock"] # ba in mishe yek action b list action haye django admin ezafeh kard 




# TOZIH  :
#  In 2 ghate code dar vaghe har 2 yek kar ra anjam midahand 
# 1:
# @admin.register(ProductClass)
# class ProductClassAdminModel(admin.ModelAdmin) :    
#     pass    
# 2 :
# admin.site.register(ProductClass ,)







@admin.register(Product)
class ProductAdmin(admin.ModelAdmin) : 
    pass   