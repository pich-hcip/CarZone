from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def index(request):
    teams=Team.objects.all()
    feature_cars= Car.objects.order_by('-created_date').filter(is_featured=True)
    latest_cars = Car.objects.all()
    # search_fields=Car.objects.values('model', 'city','year','body_style')
    model_search=Car.objects.values_list('model', flat=True).distinct()
    city_search=Car.objects.values_list('city', flat=True).distinct()
    year_search=Car.objects.values_list('year', flat=True).distinct()
    body_style_search=Car.objects.values_list('body_style', flat=True).distinct()
    context = {
        'teams':teams,
        'feature_cars': feature_cars,
        'latest_cars': latest_cars,
        # 'search_fields': search_fields,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
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
    paginator= Paginator(cars, 2)  
    page= request.GET.get('page')
    paged_cars = paginator.get_page(page)
    model_search=Car.objects.values_list('model', flat=True).distinct()
    city_search=Car.objects.values_list('city', flat=True).distinct()
    year_search=Car.objects.values_list('year', flat=True).distinct()
    body_style_search=Car.objects.values_list('body_style', flat=True).distinct()
    context = {
        'cars': paged_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request, 'pages/cars.html', context)

def contact(request):
    return render(request, 'pages/contact.html')
def dashboard(request):
    return render(request, 'pages/dashboard.html')

def login(request):
    return render(request, 'pages/login.html')

def search(request):
    cars = Car.objects.all()
    model_search=Car.objects.values_list('model', flat=True).distinct()
    city_search=Car.objects.values_list('city', flat=True).distinct()
    year_search=Car.objects.values_list('year', flat=True).distinct()
    body_style_search=Car.objects.values_list('body_style', flat=True).distinct()
    transmission_search=Car.objects.values_list('transmission', flat=True).distinct()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)
    

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact=model)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cars = cars.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)
    
    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)

    if 'transmission' in request.GET:
        transmission = request.GET['transmission']
        if transmission: 
            cars = cars.filter(transmission__iexact=transmission)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)
        
    context={
        'cars': cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
        'transmission_search': transmission_search
    }

    return render(request, 'pages/search.html', context)
def services(request):
    return render(request, 'pages/services.html')
def signup(request):
    return render(request, 'pages/signup.html')