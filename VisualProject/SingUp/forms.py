from dataclasses import fields
from pyexpat import model
from django import forms
from.models import SingUpModel
class SingUPForm(forms.ModelForm):
    class Meta:
        model=SingUpModel
        fields='__all__'

class SinginForm(forms.Form):
    Email=forms.EmailField(max_length=50)
    Password=forms.CharField(max_length=50)


