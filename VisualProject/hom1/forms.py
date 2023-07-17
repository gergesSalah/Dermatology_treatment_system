


from django import forms
from .models import home_Advert


class mainForm(forms.ModelForm):
    class Meta:
        model=home_Advert
        fields= "__all__"