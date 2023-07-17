from datetime import datetime
from distutils.command import upload
from pydoc import describe
from tkinter import CASCADE
from django.db import models
from django.forms import FilePathField
import datetime
import os





# Create your models here.
class home_Advert(models.Model):
    id_Advert =models . CharField ( max_length = 4 ) 
    prodect=models.CharField(max_length=40,null=False)
    
    describes=models.TextField(max_length=300,null=False)
    img=models.ImageField(null=True,upload_to='filepath',blank= True)
    link=models.CharField(max_length=300)
    
    def __str__(self) :
        return self.prodect