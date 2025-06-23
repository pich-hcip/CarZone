from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.


class TeamAdmin(admin.ModelAdmin):

    def image(self, obj):
        return format_html(
            '<img src="{}" style="width: 50px; height: 50px; border-radius: 10%;" />',
            obj.photo.url if obj.photo else ''
        )
    image.short_description = 'Photo'

    list_display = ('id','image', 'first_name', 'last_name', 'designation', 'created_date')
    list_display_links = ( 'id','image', 'first_name')
    search_fields = ('id', 'first_name', 'last_name', 'designation')
    list_filter = ('designation', 'created_date')
admin.site.register(Team, TeamAdmin)


class CarAdmin(admin.ModelAdmin):
    def image(self, obj):
        return format_html(
            '<img src="{}" style="width: 50px; height: 50px; border-radius: 10%;" />',
            obj.car_photo.url if obj.car_photo else ''
        )
    image.short_description = 'Photo'

    list_display = ('id','image', 'car_title', 'state', 'city', 'model', 'year', 'price', 'is_featured')
    list_display_links = ('id','image', 'car_title')
    search_fields = ('id', 'car_title', 'state', 'city', 'model', 'year')
    list_filter = ('state', 'city', 'model', 'year')
admin.site.register(Car, CarAdmin)
