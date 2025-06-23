from django.urls import path
from . import views

urlpatterns = [
    # Define your URL patterns here
    path('about/', views.about, name='about'), 
    path('car_details/<int:id>/', views.car_details, name='car_details'), 
    path('cars/', views.cars, name='cars'),  
    path('contact/', views.contact, name='contact'),  
    path('dashboard/', views.dashboard, name='dashboard'),  
    path('', views.index, name='index'), 
    path('login/', views.login, name='login'),  
    path('search/', views.search, name='search'),  
    path('services/', views.services, name='services'), 
    path('signup/', views.signup, name='signup'), 
]
