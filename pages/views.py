from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    teams=Team.objects.all()
    feature_cars= Car.objects.order_by('-created_date').filter(is_featured=True)
    context = {
        'teams':teams,
        'feature_cars': feature_cars,
    }

    return render(request, 'pages/index.html', context)
def about(request):
    teams=Team.objects.all()
    context = {
        'teams':teams,
    }
    
    return render(request, 'pages/about.html',context)

def car_details(request):

    return render(request, 'pages/car_details.html')
def cars(request):
    return render(request, 'pages/cars.html')

def contact(request):
    return render(request, 'pages/contact.html')
def dashboard(request):
    return render(request, 'pages/dashboard.html')

def login(request):
    return render(request, 'pages/login.html')

def search(request):
    # Implement search functionality here
    return render(request, 'pages/search.html')
def services(request):
    return render(request, 'pages/services.html')
def signup(request):
    return render(request, 'pages/signup.html')