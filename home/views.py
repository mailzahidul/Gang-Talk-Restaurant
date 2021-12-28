from django.shortcuts import render, redirect
from .models import *
from django.core.exceptions import MultipleObjectsReturned
from django.core.mail import send_mail
from django.contrib import messages
from restaurant.models import Meal_category
from django.conf import settings


# Create your views here.


def home(request):
    obj = AboutUs.objects.last()
    slider = Slider.objects.all()
    meal_category = Meal_category.objects.all().order_by('id')
    mealtime = MealTime.objects.all()
    try:
        feature = Feature.objects.get(is_active=True)
    except:
        feature = Feature.objects.all().last()

    context = {
        'home_content': obj,
        'meal_category': meal_category,
        'slider': slider,
        'feature': feature,
        'mealtime': mealtime
    }
    return render(request, 'pages/index.html', context)


def about(request):
    about_us = AboutUs.objects.last()
    history = History.objects.last()
    brands = Brand.objects.all()
    context = {
        'about_us': about_us,
        'history': history,
        'brands': brands
    }
    return render(request, 'pages/about.html', context)


def subscribtion(request):
    if request.method == 'POST':
        email = request.POST['email']
        Subscription.objects.create(email=email)
        messages.success(request, 'Thanks for subscribtion...')
        return redirect('about')


def custom_menu_form(request):
    return render(request, 'pages/custom_menu_form.html')


def gallery(request):
    categories = Meal_category.objects.all().order_by('id')
    context = {
        'categories': categories
    }
    return render(request, 'pages/gallery.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        sender = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']
        try:
            msg_mail = str(message) + " " + str(sender)
            Contact.objects.create(name=name, email=sender, phone=phone, subject=subject, message=message)
            send_mail(subject, msg_mail, sender, ['mailzahidul@gmail.com'], fail_silently=False)
            messages.success(request, 'We get your message and reply shortly...')
        except:
            messages.error(request, "Failed to send message.")

    shops = Shop.objects.filter(active=True).order_by('id')

    context = {
        'shops': shops
    }

    return render(request, 'pages/contact.html', context)
