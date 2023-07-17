from re import X
from django.http import HttpResponse
from django.shortcuts import redirect, render
from numpy import append

from services import AiClassification
from .models import areas, patientdiseases,patient,diseases,areas
from .forms import patientdiseasesform

# Create your views here.

def showindexPage(request):
    return render(request,'services/service.html')


def retrievepatientdisease(request):
    x = patientdiseases.objects.all()
    return render(request,'services/retrieveALLdiseases.html',{'disease':x}) 


def inserphotoV(request):
    picture_name = 123
    result = "Nthing"
    
    if request.method == 'POST':
        form = patientdiseasesform(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            cd = form.cleaned_data
            picture_name = cd['picture']
            Accuracy,result = AiClassification.classify(picture_name)
          
           
            print('=================================================================== ')
            print(request)
            # picture = 323
            return render(request,'services/showResult.html',{'result':result,'Accuracy':Accuracy})
    else:
        form = patientdiseasesform()
    return render(request, 'services/Examination.html', {'form' : form})#,'picture': picture_name
  

    # form = patientdiseasesform(request.POST or None , request.FILES or None)
    # if form.is_valid():
        
    #     form.save()
    #     return redirect('servicesN')
    
    # return render(request,'services/Examination.html',{'form':form})
 

def retrieve_diseasesV(request):
    disease = diseases.objects.all()
    
    return render(request,'services/showALLdiseases.html',{'disease':disease})

disea=''
def disease_infoV(request,dises_id):
    disease = diseases.objects.get(pk = dises_id)
    return render(request,'services/disease_informatioin.html',{'disease':disease})


def retrieve_areasV(request):
    area = areas.objects.all()
    return render(request,'services/showALLareas.html',{'areas':area})


def areas_infoV(request,areas_id):
    area = areas.objects.get(pk = areas_id)
    return render(request,'services/areas_informatioin.html',{'areas':area})
