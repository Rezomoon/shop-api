from django.db import models
from django.contrib.auth.models import User 
from django.conf import settings
# 




# ABSTRACT MODEL :
class AuditableModel(models.Model) : 

    created_by  = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.SET_NULL , null = True , related_name= "created" , editable=False) # get_user_model()
    created_at  = models.DateTimeField(auto_now_add=True , editable=False)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.SET_NULL , null = True ,  related_name= "modified" , editable=False)  # Va Chon 2ta field dar b 1 model fk mikhore hatman bayad az related_name estefadeh shavad
    modified_at = models.DateTimeField(auto_now=True , editable=False)
    
    class Meta : 
        abstract = True
        