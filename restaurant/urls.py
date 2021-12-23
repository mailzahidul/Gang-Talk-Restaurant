from django.urls import path
from . import views
urlpatterns = [

    path('offers/', views.offers, name="offers"),
    path('food_details/<int:id>', views.food_details, name='food_details'),
    path('reservation/', views.reservation, name='reservation'),
    path('menu/', views.menu, name='menu'),
    path('catering/', views.catering, name='catering'),
    path('catering_details/<int:id>', views.catering_details, name='catering_details'),
    path('catering_mail/', views.catering_mail, name="catering_mail"),
    path('custome_order/', views.custome_order, name="custome_order")
]