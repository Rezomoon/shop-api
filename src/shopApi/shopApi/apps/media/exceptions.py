
from rest_framework.exceptions  import APIException
# Chon darim az RestFrameWork estefadeh mikonim behtar hastesh az APIexception  ers bari konim va dar 
# laye haye payeen tar behtare k az exception ers begirim


# in yek excepyion bussinisi hastesh !
class DuplicateImageException(APIException) :
    
    pass