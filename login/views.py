from django.contrib import messages
from os import name
from django.db import models
from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import date, datetime
from django.contrib.auth.models import User
from django.contrib.auth import login, logout,authenticate

# Create your views here.
def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/main")
        else:
            return render(request, "login.html")
    return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    return redirect('/login')

def main(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'main.html')
