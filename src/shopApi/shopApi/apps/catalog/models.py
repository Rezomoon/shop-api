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
    slug        = models.SlugField()


    objects     = CategoryQuerySet.as_manager()



    def __str__(self): 
        # Dar django admin ham ba hamin field neshan dadeh mishavad 
        return self.title
        
    class Meta : 

        verbose_name        = "Category"
        verbose_name_plural = "Categories"