from django.db import models
from treebeard.mp_tree import MP_Node
from .managers import CategoryQuerySet
from shopApi.libs.db.fields import UpperCaseCharField

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
    
    options      = models.ManyToManyField('option' , blank=True  ) # Chon Payeen tar class Option Tarif Shodeh ast bayad Toye qouttaion tarif Shavad 

    # ersal lazem dare ya na
    require_shipping = models.BooleanField(default=True)


   # @property => ba in mishe k az func zir b onvane yek prorty va field estefadeh kard masalan dar django Admin
    def has_attribute(self ) :
        return self.attributes.exists()
    def __str__(self):
        return self.title
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
    class Meta : 
        verbose_name        = "Product Attribute"
        verbose_name_plural = "Product Attributes"


class Option(models.Model) : 

    class OptionTypeChoice(models.TextChoices) :
        text    = "text" 
        integer = "integer"
        float   = "float"
        option  = "option"
        multi_option    = "multi_option"
    title           = models.CharField(max_length=64)
    type            = models.CharField(max_length = 16    , choices = OptionTypeChoice.choices , default = OptionTypeChoice.text)
    option_group    = models.ForeignKey(OptionGroup     , on_delete=models.PROTECT , null = True , blank=True)  # Ba PROTECT ejazeh Hazf dadeh nemishavad
    required        = models.BooleanField(default=False)
    class Meta : 
        verbose_name        = "Option"
        verbose_name_plural = "Options"


class Product(models.Model) :

    class ProductTypeChoice(models.TextChoices): # in baraye ine k befahmim strucure chie Yani aya az in product faghat yek noo mashool hastesh ya chandin zir majmooe Dare
        standalone  = "standalone"
        parent      = "parent"
        child       = "child"
    structure   = models.CharField(max_length=20 , choices=ProductTypeChoice.choices , default=ProductTypeChoice.standalone)
    parent      = models.ForeignKey("self" , related_name="children", on_delete=models.CASCADE , null = True , blank=True) # attribute children
    title       = models.CharField(max_length=128 ,  null = True , blank=True)


    # Custom Field : Vaghtie k ma mikhayeem field mokhtase khodemoon ro dashte bashim
    upc         = UpperCaseCharField(max_length=14 , unique=True,null   = True ,  blank=True) # universal product code => globaly unique code for All Products

    is_public   = models.BooleanField(default=True)
    slug        = models.SlugField(unique= True , allow_unicode=True)
    meta_title  =  models.CharField(max_length=128 , null=  True , blank= True)     #ITs For SEO
    meta_discription = models.TextField(null= True , blank=True)

    product_class   = models.ForeignKey(ProductClass , on_delete= models.PROTECT , null= True , blank= True , related_name="products") # attributee k az productClass Gharare bereseh=> related_name 


    # Chon Ma yek Rabeteh Many to Many Darim va django b sorate default dare yek tablee mojaza baraye data haye ma misaze
    # vali chon ma data haye dige iyee mikhahim b oon table ezafe h konim bayad b sorate zir amal konim through = ProductAttributeValue
    # Yani ma darim b django migim k in rabeteh many to many ro az tariq in jadval manage kon
    attributes      = models.ManyToManyField(ProductAttribute , through="ProductAttributeValue")


    class Meta : 
        verbose_name        = "Product"
        verbose_name_plural = "Products"

# Tabeli k b jaye table default django sakhte mishavad 
class ProductAttributeValue(models.Model) : 
    product     = models.ForeignKey(Product , on_delete=models.CASCADE)
    attribute   = models.ForeignKey(ProductAttribute , on_delete=models.CASCADE)

    value_text      = models.TextField(null = True , blank = True)
    value_integer   = models.IntegerField(null = True , blank = True)
    value_float     = models.FloatField(null = True , blank=True)

    value_option            = models.ForeignKey(OptionGroupValue , on_delete=models.PROTECT , null= True , blank=True)
    value_multi_option      = models.ManyToManyField(OptionGroupValue , blank=True,related_name="multi_valued_attribute_value")    
    recommended_products    = models.ManyToManyField("catalog.Product" , through="ProductRecommendation" , blank= True) # chon ProductRecommendation Class payeen Tarif Shode Dar Qoutetion mizarimesh


    class Meta : 
        verbose_name        = "Product"
        verbose_name_plural = "Products"
        unique_together     = ("product" , "attribute")

class ProductRecommendation(models.Model) : 
    # JADVALE VASET

    primary         = models.ForeignKey(Product , on_delete=models.CASCADE , related_name= "primary_recommendation")
    recommendation  = models.ForeignKey(Product , on_delete=models.CASCADE)

    # Ta in Bala Default Table khode Django mishe
    rank            = models.PositiveSmallIntegerField(default=0)
    class Meta      :
        unique_together     = ("primary" , "recommendation")
        ordering            = ("primary","-rank")