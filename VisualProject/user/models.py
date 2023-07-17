from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=30,null=True)

    phone = models.CharField(max_length=30,null=True)
    
    special = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=100,null=True)
    doc_img = models.ImageField(upload_to="doc_img/",)
    examination_price = models.CharField(max_length=20,null=True)
    
    def __str__(self) -> str:
        return self.name



class Patient(models.Model):
    name = models.CharField(max_length=30,null=True)
    email = models.EmailField(max_length=30,null=True)
    gender = models.CharField(max_length=50,null=True)
    phone = models.CharField(max_length=30,null=True)
    address = models.CharField(max_length=100,null=True)
    birth = models.DateField(max_length=20,null=True)
    bloodgroup = models.CharField(max_length=5,null=True)
   
      
    
    def __str__(self) -> str:
        return self.name        