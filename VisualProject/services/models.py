
from pyexpat import model
from tkinter.tix import INTEGER
from django.db import models
from django.forms import CharField, IntegerField

# Create your models here.


class patient(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self) -> str:
        return self.name
    


class patientdiseases(models.Model):
    picture = models.ImageField(null=True,upload_to="images/")
    date = models.DateField(auto_now_add=True,null=True)
    # Symptoms = models.CharField(max_length=200,)
    # patient = models.ForeignKey(patient,related_name="patientName",on_delete=models.CASCADE,null=True)
    
    def __str__(self) -> str:
        return self.picture
    
    
class diseases(models.Model):
    code = models.CharField(max_length=25,null=True)
    name = models.CharField(max_length=50)
    reg_date = models.DateTimeField(auto_now=True,null=True)
    description = models.CharField(max_length=500)
    
    def __str__(self) -> str:
        return self.name
    
    
class treatments(models.Model):
    disease = models.ForeignKey(diseases,related_name='treat_dises',on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    Indications = models.CharField(max_length=500)
    Contraindications = models.CharField(max_length=500,null=True)
    price = models.FloatField()
    
    def __str__(self) -> str:
        return self.name
    
    
    
class areas(models.Model):
    number = models.CharField(max_length=25,null=True)
    name = models.CharField(max_length=50)
    reg_date = models.DateTimeField(auto_now=True,null=True)
    description = models.CharField(max_length=500)
    
    def __str__(self) -> str:
        return self.name
    
    
class pharmacies(models.Model):
    area = models.ForeignKey(areas,related_name='area_pharc',on_delete=models.CASCADE,null=True)#disease , treat_dises
    name = models.CharField(max_length=50,null=True)#name
    phone = models.IntegerField(null=True)#Indications
    address = models.CharField(max_length=500,null=True)#Contraindications
    rate = models.FloatField()#price
    
    def __str__(self) -> str:
        return self.name