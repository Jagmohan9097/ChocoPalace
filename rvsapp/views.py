from django.contrib import messages
from os import name
from django.db import models
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product
from datetime import date, datetime
from .models import Contact

#Create your views here.
result = "Jagmohan"
def jags(request,*args, **kwargs):
    return render(request, 'home.html')

def form(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        query = request.POST.get('query')
        contact = Contact(name=name, email=email, phone=phone, query=query, date=datetime.today())
        contact.save()
        messages.success(request, " ")
    return render(request, 'contact.html')

def service(request):
    return render(request, 'service.html')

def home(request):
    return render(request, 'home.html')





def data(request):
    n = request.POST.get("name")
    e = request.POST.get("email")
    p = request.POST.get("phone")
    g = request.POST.get("gender")
    c = request.POST.get("country")
    tech = request.POST.getlist("technology[]")
    return render(request, 'data.html', {"name":n, "email":e, "phone":p, "gender":g, "country": c, "technology":tech})


# def jags(*args, **kwargs):
#     return HttpResponse("<h1>Django is Nice</h1>")

# def user(*args, **kwargs):
#     return HttpResponse("<h1>Django Admin</h1>")