from django.shortcuts import render,redirect

users=[]
# Create your views here.
from.forms import SingUPForm
def SingUpFun(requset):
    form=SingUPForm(requset.POST or None,requset.FILES or None)
    if form.is_valid():
        user=form.save()
        users.append(user.pk)
        return redirect('all_ads')

    
    return render(requset,'SingUp/SingUpPage.html',{'form':form})




def adminPage(reguset):
    return render(reguset,'SingUp/index2.html')   

from.forms import SinginForm
from.models import SingUpModel

def SinginFun(requset):
    users.clear()
    
    m=''
    us=''
    Email=''
    password=''
    form=SinginForm()
    if requset.method=='POST':
        form=SinginForm(requset.POST)
        if form.is_valid():
            cd =form.cleaned_data
            
            Email=cd['Email']
            password=cd['Password']
    data=SingUpModel.objects.all()
    user=''
    for item in data:
        if item.Email==Email and item.Password ==password:
            user=item.pk
            users.append(user)
            print('======================================')
            print(users[0])
            print('======================================')
            return redirect('all_ads')
        else:
            m="Email or Password is Not Valid"    
        
    return render(requset,'SingUp/login.html',{'form':form,'user':us,'messg':m})


def testFun(requset):
    form=SingUPForm()
    user=users[0]
    
    date=SingUpModel.objects.get(pk=user)
    date.Username='Samy'
    return render (requset,'profilePatient/profile.html',{'form':form ,'user':user,'date':date})





