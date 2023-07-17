from datetime import datetime
from mimetypes import init
from turtle import width
from django.db import models

class SingUpModel(models.Model):
    Firstname=models.CharField(max_length=30)
    Lastname=models.CharField(max_length=30)
    Username=models.CharField(max_length=30)
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=30)
    Brith_Date=models.DateField(null=True,default=datetime.now)
    phone=models.IntegerField( null=True )
    address=models.CharField(max_length=100)
    def __str__(self) :
        return self.Username
    
