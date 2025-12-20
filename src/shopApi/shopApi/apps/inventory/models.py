from django.db import models

# Create your models here.

class StockRecord(models.Model) : 
    product     = models.ForeignKey("catalog.Product" , on_delete= models.CASCADE , related_name="stockrecords") # Baraye fk az app dige behtare k ba ' va adress
    # biarim na k import konim

    # standard keep unit :
    sku         = models.CharField(max_length=64 ,null=True , blank=True , unique=True) # Hamoon joori k migofim har mahsoli too donia yek code moshakhas dare 
    # mA dar Anbar Darimoon Ham yek code moshakhas darim !

    buy_price   = models.PositiveBigIntegerField(null=True ,blank=True)

    sales_price = models.PositiveBigIntegerField()

    num_stock   = models.PositiveIntegerField(default=0)

    threshold_low_stack = models.PositiveIntegerField(null=True , blank=True)