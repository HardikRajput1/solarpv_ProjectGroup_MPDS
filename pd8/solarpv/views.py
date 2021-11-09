from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'solarpv/index.html')

def register(request):
    return render(request,'solarpv/register.html')

def signin(request):
    return render(request,'solarpv/signin.html')

def portalform(request):
    return render(request,'solarpv/portalform.html')

def location_form(request):
    return render(request,'solarpv/location_form.html')

def product_form(request):
    return render(request,'solarpv/product_form.html')

def test_standard_form(request):
    return render(request,'solarpv/test_standard_form.html')

def certificate_form(request):
    return render(request,'solarpv/certificate_form.html')

def client_form(request):
    return render(request,'solarpv/client_form.html')