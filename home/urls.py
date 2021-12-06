from django.urls import path
from . import views



urlpatterns=[
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('reservation/', views.reservation, name='reservation'),
    path('catering/', views.catering, name='catering'),
    path('catering_details/', views.catering_details, name='catering_details'),
    path('offers/', views.offers, name='offers'),
    path('food_details/', views.food_details, name='food_details'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('custom_menu_form/', views.custom_menu_form, name='custom_menu_form'),
]