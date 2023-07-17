from datetime import datetime
from django import forms

class profileForm(forms.Form):
    Firstname=forms.CharField(max_length=30)
    Lastname=forms.CharField(max_length=30)
    Username=forms.CharField(max_length=30)
    Email=forms.EmailField(max_length=50)
    Password=forms.CharField(max_length=30)
    Brith_Date=forms.DateField(initial=datetime.now)
    phone=forms.IntegerField( )
    address=forms.CharField(max_length=100)