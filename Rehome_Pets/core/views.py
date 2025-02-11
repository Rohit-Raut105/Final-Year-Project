import random
import string
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

def register(request):
    if request.method=='POST':
       fname=request.POST['first_name']
       Lname=request.POST['last_name']
       Email=request.POST['email']
       username=request.POST['username']
       password=request.POST['password']
       password2=request.POST['Cpassword']
       if User.objects.filter(username=username).exists():
           messages.error(request,'UserName Already Exist')
       else:
        if not password==password2:
           messages.error(request,'password dosent match ')
        else:
            if len(password) <= 8:
               messages.error(request,"password is less that 8 charectars long") 
            else:
                contains_special=False
                for i in password:
                   char= ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']
                   if i in char:
                      contains_special=True
                      break
                if contains_special==True:
                    request.session['user_data'] = {
                            'first_name': fname,
                            'last_name': Lname,
                            'email': Email,
                            'username': username,
                            'password': password
                        }
                    otp = random.randint(100000, 999999)
                    print(otp)
                    request.session['ottp'] = otp
                    request.session['email'] = Email
                    subject = "OTP for your Rehome Pets Login"
                    message = f"Dear User, {otp} is your OTP for RehomePets. For security reasons, do not share it with others. Best regards, ClassSphere."
                    from_email = settings.EMAIL_HOST_USER
                    recipient_list = [Email]
                    try:
                        send_mail(subject, message, from_email, recipient_list)
                        return redirect('otp')
                    except Exception as e:
                        messages.error(request,f'An error has occured ! {e}')
                else:
                    messages.error(request,'Please use a  special charectar')
    return render(request,'register.html')

def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        Flag = authenticate(request, username=username, password=password)  # FIXED
        
        if Flag is not None:
            login(request, Flag)
            return redirect('home')  # Redirects to 'home' after successful login
        else:
            messages.error(request, "Invalid username or password")  # Pass error message

    return render(request, 'login.html')

def OTP(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('OTPentered')
        sent_otp = request.session.get('ottp')
        user_data = request.session.get('user_data')
        if not user_data:
            messages.error(request, "Session expired! Please register again.")
            return redirect('register')

        first_name = user_data.get('first_name')
        last_name = user_data.get('last_name')
        email = user_data.get('email')
        username = user_data.get('username')
        password = user_data.get('password')
        if entered_otp == str(sent_otp):
            try:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    username=username,
                    password=password
                )
                messages.success(request, "Registration successful! Please log in.")
                request.sessionI.flush()
                return redirect('login')  
            except Exception as e:
                messages.error(request, f"Error creating user: {e}")
        else:
            messages.error(request, "Invalid OTP. Please try again.")
    return render(request, 'OTPpage.html')

def home(request):
    return render(request,'Home.html')