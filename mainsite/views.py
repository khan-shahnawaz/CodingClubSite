from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .codeforces import *
# Create your views here.
def index(request):
    navbar=Navbar.objects.all()
    profiles= profile.objects.all()
    slideshows= slideshow.objects.all()
    rating= get_best(profiles)
    return render(request,'index.html',{'navbars':navbar,'best_rating':rating,'slideshow':slideshows,'slide_max':len(slideshows)})
def login(request):
    navbar=Navbar.objects.all()
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
        return render(request,'login.html',{'navbars':navbar})
def logout(request):
    auth.logout(request)
    messages.info(request,'Logged out successfully')
    return redirect('/')
def register(request):
    navbar=Navbar.objects.all()
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        cfid=request.POST['cfid']
        password2=request.POST['password2']
        batch=request.POST['batch']
        if password!=password2:
            messages.info(request,'Both passwords should be same')
            return redirect('register')
        else:
            if User.objects.filter(email=email).exists():
                user = User.objects.get(email=email)
                messages.info(request,'Email already registered!')
                return redirect('register')
            else:
                if profile.objects.filter(cfid=cfid).exists():
                    messages.info(request,'Codeforces Id already registered! If its your id, please contact Admin')
                    return redirect('register')
                else:
                    if authenticate(cfid)==False:
                        messages.info(request,"Invalid Codeforces Id")
                        return redirect('register')
                    else:
                        user=User.objects.create_user(username=email,email=email,first_name=firstname,last_name=lastname,password=password)
                        User.save(user)
                        user_profile=profile()
                        user_profile.user=user
                        user_profile.cfid=cfid
                        user_profile.batch=batch
                        user_profile.cf_rating=get_rating(cfid)
                        user_profile.save()
                        messages.info(request,"Success")
                        messages.info(request,"Your Current Rating: "+str(user_profile.cf_rating))
                        return redirect ('login')
    else:
        return render (request,'register.html',{'navbars':navbar})
def leaderboard(request):
    return(render(request,'leaderboard.html'))
def contact(request):
    return(render(request,'contact.html'))
def resources(request):
    return(render(request,'resources.html'))