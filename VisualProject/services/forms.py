# from distutils.command.upload import upload
# from pyexpat import model
# from dataclasses import field
# from pyexpat import model
from django import forms

from services.models import patient,patientdiseases

class patientdiseasesform(forms.ModelForm):
    class Meta:
        model=patientdiseases
        fields= ['picture']
        #'Symptoms','patient'
        