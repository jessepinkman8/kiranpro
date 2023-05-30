from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.shortcuts import render
from app1.models import abc
from app1.models import abc1
from app1.models import abc2
from app1.models import abc3

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def fashion(request):
    obj = abc.objects.all()
    return render(request,'fashion.html',{'qwe':obj})

def personal(request):
    objq = abc1.objects.all()
    return render(request,'personal.html',{'asd':objq})

def product(request):
    objw = abc2.objects.all()
    return render(request,'product.html',{'zxc':objw})

def services(request):
    return render(request,'services.html')

def wedding(request):
    obje = abc3.objects.all()
    return render(request,'wedding.html',{'iop':obje})

