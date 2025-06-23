from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def index(request):
    teams=Team.objects.all()
    feature_cars= Car.objects.order_by('-created_date').filter(is_featured=True)
    latest_cars = Car.objects.all()
    context = {
        'teams':teams,
        'feature_cars': feature_cars,
        'latest_cars': latest_cars,
    }

    return render(request, 'pages/index.html', context)
def about(request):
    teams=Team.objects.all()
    context = {
        'teams':teams,
    }
    
    return render(request, 'pages/about.html',context)

def car_details(request, id):
    single_car = get_object_or_404(Car, id=id)
    context = {
        'single_car': single_car,
    }
    return render(request, 'pages/car_details.html', context)
def cars(request):
    cars = Car.objects.all()
    paginator= Paginator(cars, 3)  
    page= request.GET.get('page')
    paged_cars = paginator.get_page(page)
    context = {
        'cars': cars,
    }
    return render(request, 'pages/cars.html', context)

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