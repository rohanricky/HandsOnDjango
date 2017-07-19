# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from authe.forms import SignIn

from authe.models import signin

from django.contrib.auth import authenticate,login

from django.contrib.auth.models import User

# Create your views here.
def x(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        context = {'username':username}
        user=User(username=username,password=password)
        user.set_password(user.password)
        user.save()
    return render(request,'authe/x.html',context)

def log(request):
    username = request.POST['username']
    password=request.POST['password']
    user = authenticate(request,username=username,password=password)
    if user is not None:
       login(request,user)
       return render(request,'authe/success.html')

    else: 
        return render(request,'authe/contact.html')
"""def log(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render(request,'authe/success.html',{'state':state})   """

def access(request):
    form = SignIn(request.POST)
    return render(request,'authe/signin.html',{'form':form})

def contact(request):
	form = SignIn(request.POST)
	return render(request,'authe/contact.html',{'form':form})

def forgot(request):
    form = ForgotPassword(request.POST)
    return render(request,'authe/forgot.html',{'form':form})
