from django.shortcuts import render

def aboutFun(requset):
    return render(requset,'about/about.html')