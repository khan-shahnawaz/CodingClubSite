from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Navbar
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.
def index(request):
    navbar=Navbar.objects.all()
    return render(request,'index.html',{'navbars':navbar})
def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        try:
            user = User.objects.get(email=email)
        except:
            messages.info(request,'Invalid Login')
            return redirect('login')
       
        else:
            if user.check_password(password):
                auth.login(request,user)
                return redirect('/')
            else:
                messages.info(request,'Invalid Login')
                return redirect('login')
    else:        
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')