from django.shortcuts import render

# Create your views here.
from .models import Doctor,Patient

def retriveDoctor(request):
    x = Doctor.objects.all()
    return render(request,'user/listalldoctor.html',{'doctor':x})


from .forms import DoctorForm
from django.shortcuts import redirect

def addnewDoctor(request):
    form = DoctorForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('list_all_Doctor')


    
    return render(request,'user/new_doctor.html',{'form':form})





