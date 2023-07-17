"""VisualProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from SingUp.views import SingUpFun,adminPage,SinginFun,testFun
from profilePatient.views import profileFun
from user.views import retriveDoctor
from user.views import addnewDoctor
from user.views import retriveDoctor
from user.views import addnewDoctor
from hom1.views import retreveadv,add_adv
from about.views import aboutFun
from contact.views import contactFun
from services.views import showindexPage,retrievepatientdisease,inserphotoV,retrieve_diseasesV,disease_infoV,retrieve_areasV,areas_infoV





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', adminPage ,name='admin'),
    path('SingUp',SingUpFun ),
    path('SingIn',SinginFun ,name='LogIN' ),
    path('test',testFun ,name='test1' ),
    path('profile',profileFun ,name='profilepatient' ),
    path('docALL',retriveDoctor,name ='list_all_Doctor'),
    path('NewDoctor',addnewDoctor,name ='add_new_Doctor'),
    path('dis_adv', retreveadv,name='all_ads'),
    path('addadv',add_adv,name='add_new_ads' ),
    path('contact',contactFun,name='contactme' ),
    path('about',aboutFun,name='aboutme' ),
    path('service', showindexPage,name='servicesN'),
    path('patientdeiseasesAllL', retrievepatientdisease,name='patientdeiseasesAllN'),
    path('insertphotoL', inserphotoV,name='insertphotoN'),
    path('retrieve_diseasesL',retrieve_diseasesV,name='retrieve_diseasesN'),
    path('desiease_infoL/<int:dises_id>',disease_infoV,name='disease_infoN'),
    path('retrieve_areasL',retrieve_areasV,name='retrieve_areasN'),
    path('areas_infoL/<int:areas_id>',areas_infoV,name='areas_infoN'),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

  
# if settings.DEBUG:
#         urlpatterns += static(settings.MEDIA_URL,
#                               document_root=settings.MEDIA_ROOT)