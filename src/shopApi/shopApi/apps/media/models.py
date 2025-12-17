from django.db import models

# Create your models here.


class Image(models.Model) :

    title   = models.CharField(max_length=128 , null= True , blank=True)
    image   = models.ImageField( width_field="width" , height_field="height" , upload_to="images/")


    width   = models.IntegerField(editable=False)
    height  = models.IntegerField(editable=False)

    file_hash = models.CharField(max_length=40 , db_index=True)
    file_size = models.PositiveIntegerField(null=True)


    # Focal Point B ONvane Yek Noghte Kanonie Ax Ham mitonim begirim 
    focal_point_x = models.PositiveIntegerField(null= True, blank=True)
    
    focal_point_y      = models.PositiveIntegerField(null= True, blank=True)
    focal_point_width  = models.PositiveIntegerField(null= True, blank=True)
    focal_point_height = models.PositiveIntegerField(null= True, blank=True)

    def save(self, *args , **kwargs):

        self.file_size = self.image.size
        return super().save(*args , **kwargs)