from django.shortcuts import render,redirect
from.forms import contactForm

def contactFun(requset):
    
    form=contactForm(requset.POST or None, requset.FILES or None)
   
    if form.is_valid():
            form.save()
            return redirect('all_ads')
        

    return render(requset,'contact/contact.html',{'form':form})
