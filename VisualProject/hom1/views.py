
from django.shortcuts import render
from.models import home_Advert
from.forms import mainForm
from django.shortcuts import redirect
# Create your views here.

def retreveadv(request):
   a={ 'description': home_Advert.objects.all()}

   return render(request,'hom1/main.html',a)



  

def add_adv(requset):
    form=mainForm()
   
    if requset.method=='POST':
        form=mainForm(requset.POST or None, requset.FILES or None)
        form
        if form.is_valid():
            form.save()
            return redirect('all_ads')


    return render(requset,'hom1/new_ads.html',{'form':form })




