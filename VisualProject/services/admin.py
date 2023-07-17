from django.contrib import admin

# Register your models here.

from .models import patientdiseases,patient,diseases,treatments,areas,pharmacies

admin.site.register((patientdiseases,patient,diseases,treatments,areas,pharmacies))