from django.db import models
from treebeard.mp_tree import MP_Node
from .managers import CategoryQuerySet

# Create your models here.

class Category(MP_Node):
    title       = models.CharField(max_length=255 , db_index=True)
    describtion = models.CharField(max_length=2048 , null=True , blank=True) 
    # null=> Yani baraye dataBAse ghabele ghabol mishe k khali bashad
    # blank => Yani django form Ghabol bokone khali vared shodane etelaat ro (input data Mitone Khali Bashe !)
    is_public   = models.BooleanField(default=True)
    slug        = models.SlugField(unique= True , allow_unicode=True)


    objects     = CategoryQuerySet.as_manager()



    def __str__(self): 
        # Dar django admin ham ba hamin field neshan dadeh mishavad 
        return self.title
        
    class Meta : 

        verbose_name        = "Category"
        verbose_name_plural = "Categories"

class OptionGroup(models.Model) :

    title   = models.CharField(max_length=255 , db_index=True)
    
    def __str__(self):
        return self.title
    class Meta : 
        verbose_name        = "Option Group"
        verbose_name_plural = "Option Groups"


class OptionGroupValue(models.Model) :

    title   = models.CharField(max_length=255 , db_index=True)

    group   = models.ForeignKey(OptionGroup , on_delete=models.CASCADE) # Rabete YEk B Chand Ba OptionGroup
    
    def __str__(self):
        return self.title
    class Meta : 
        verbose_name        = "Option Group Value"
        verbose_name_plural = "Option Group Values"


class ProductClass(models.Model) :

    title       = models.CharField(max_length=255 ,db_index=True)
    slug        = models.SlugField(unique= True , allow_unicode=True)
    describtion = models.CharField(max_length=2048 , null=True , blank=True)  

    track_stock = models.BooleanField(default=True)

    # ersal lazem dare ya na
    require_shipping = models.BooleanField(default=True)

    def has_attribute(self ) :
        return self.attributes.exists()
    
    class Meta : 
        verbose_name        = "Product"
        verbose_name_plural = "Products"

        

class ProductAttribute(models.Model) : 

    class AttributeTypeChoice(models.TextChoices) :
        text    = "text" 
        integer = "integer"
        float   = "float"
        option  = "option"
        multi_option    = "multi_option"
    title           = models.CharField(max_length=64)
    type            = models.CharField(max_length=16    , choices=AttributeTypeChoice.choices , default=AttributeTypeChoice.text)
    option_group    = models.ForeignKey(OptionGroup     , on_delete=models.PROTECT , null = True , blank=True)  # Ba PROTECT ejazeh Hazf dadeh nemishavad 
    product_class   = models.ForeignKey(ProductClass    , on_delete=models.CASCADE , null =True, related_name= "attributes")               # Rabte yek b chand 
    required        = models.BooleanField(default=False)