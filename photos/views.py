from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Image, Category, Location

# Create your views here.

def home(request):
    images= Image.objects.all()
    return render(request, "home.html", {"images":images})

def about(request):
    return render(request,"about.html")

