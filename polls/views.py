from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from polls.models import Feedback,signin
from polls.forms import ContactForm,SignIn
from django.contrib.auth import authenticate,login

def contact(request):
    form = SignIn()
    return render(request,'polls/contact.html',{'form':form})

def thanks(request):
    if request.method == "POST":
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        sender = request.POST.get('sender')
        context = {'subject':subject,'message':message,'sender':sender}
        Feedback.objects.create(subject=subject,message=message,sender=sender)
    return render(request,'polls/thanks.html',context)

def x(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        context = {'username':username}
        signin.objects.create(username=username,password=password)
    return render(request,'polls/x.html',context)

def login(request):
    username = request.POST['username']
    password=request.POST['password']
    user = authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
        return render(request,'polls/success.html')

    else: 
        return render(request,'polls/contact.html')

def access(request):
    form = SignIn(request.POST)
    return render(request,'polls/login.html',{'form':form})

