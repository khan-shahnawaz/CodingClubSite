from django.shortcuts import render
from django.http import HttpResponse
from .models import Navbar
# Create your views here.
def index(request):
    navbar=Navbar.objects.all()
    return render(request,'index.html',{'navbars':navbar})