from django import forms
from.models import ContactModel
class contactForm(forms.ModelForm):
    class Meta:
        model=ContactModel
        fields= "__all__"