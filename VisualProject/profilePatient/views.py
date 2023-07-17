from dataclasses import dataclass
from dis import dis
from django.shortcuts import render
from SingUp.views import users
from SingUp.models import SingUpModel

from services.models import diseases

from.forms import profileForm


def profileFun(requset):

    user= users[0]
   
    date=SingUpModel.objects.get(pk=user)
  
    form=profileForm(requset.POST or None,requset.FILES or None)
    if form.is_valid():
        cd=form.cleaned_data
        n1=date.Firstname=cd['Firstname']
        n2=date.Lastname=cd['Lastname']
        n3=date.Username=cd['Username']
        n4=date.Email=cd['Email']
        n5=date.Password=cd['Password']
        n6=date.Brith_Date=cd['Brith_Date']
        n7=date.phone=cd['phone']
        n8=date.address=cd['address']
        total=SingUpModel(
            pk=user,
            Firstname=n1,
            Lastname=n2,
            Username=n3,
            Email=n4,
            Password=n5,
            Brith_Date=n6,
            phone=n7,
            address=n8 
            )
        total.save()
    form= profileForm()  
    date=SingUpModel.objects.get(pk=user) 
    return render (requset,'profilePatient/profile.html',{'form':form ,'user':user,'date':date,})