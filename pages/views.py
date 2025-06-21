from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')
def about(request):
    
    return render(request, 'pages/about.html')

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