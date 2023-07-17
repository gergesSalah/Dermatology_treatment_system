from cv2 import phase
from django.db import models

# Create your m]
# odels here.
class ContactModel(models.Model):
    YourFullNmae=models.CharField(max_length=100)
    YourEmail=models.CharField(max_length=100)
    YourPhone=models.IntegerField()
    QueryTopic=models.CharField(max_length=100)

    YourMessage=models.TextField(max_length=200 )
    
    
    def __str__(self) :
        return self.YourFullNmae