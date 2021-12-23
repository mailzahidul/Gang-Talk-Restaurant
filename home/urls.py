from django.urls import path
from . import views



urlpatterns=[
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('custom_menu_form/', views.custom_menu_form, name='custom_menu_form'),
    path('subscribtion/', views.subscribtion, name='subscribtion'),
]