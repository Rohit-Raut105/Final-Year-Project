from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
def register(request):
    if request.method=='POST':
       fname=request.POST['first_name']
       Lname=request.POST['last_name']
       Email=request.POST['email']
       username=request.POST['username']
       password=request.POST['password']
    #   1. Unique username
    #   2. check if both password matches 
    #   3. check if password length greater than 10
    #   4. check if password has special charectar capital letters and numbers  
       user=User.objects.create_user(first_name=fname,last_name=Lname,email=Email,username=username,password=password)
       user.save()
    return render(request,'register.html')

def loginUser(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        Flag=authenticate(username=username,password=password)
        if Flag is not None:
            login(request,Flag)
            return HttpResponse('This is Homepage')
        else:print('milena')
    return render(request,'login.html')

