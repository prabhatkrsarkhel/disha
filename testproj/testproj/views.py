# i have created this file
from django.http import HttpResponse
from django.shortcuts import render
from .forms import user_reg_form


#def home (request):
#    return HttpResponse("Hello Prabhat")
def home (request):
    return render(request,'home.html')
def index(request):
    return render(request,'index.html')
def user_reg(request):
    return render(request,'user_reg.html')
def owner_reg(request):
    return render(request,'owner_reg.html')
def login(request):
    return render(request, 'login.html')