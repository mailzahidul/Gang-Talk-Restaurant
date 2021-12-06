from django.shortcuts import render
from .models import *
from django.core.exceptions import MultipleObjectsReturned
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')


def menu(request):
    return render(request, 'pages/menu.html')


def reservation(request):
    return render(request, 'pages/reservation.html')


def catering(request):
    return render(request, 'pages/catering.html')


def catering_details(request):
    return render(request, 'pages/catering_details.html')


def custom_menu_form(request):
    return render(request, 'pages/custom_menu_form.html')


def offers(request):
    return render(request, 'pages/offers.html')


def food_details(request):
    return render(request, 'pages/food_details.html')


def blog(request):
    return render(request, 'pages/blog.html')


def single_blog(request):
    return render(request, 'pages/single_blog.html')


def gallery(request):
    return render(request, 'pages/gallery.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        sender = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']
        try:
            msg_mail = str(message)+" " + str(sender)
            send_mail(subject , msg_mail, sender ,  ['mailzahidul@gmail.com'], fail_silently=False)
            messages.success(request, 'We get your message and reply shortly...')
        except:
            messages.error(request, "Failed to send message.")
    

    try:
        obj = LocationDetails.objects.get(active=True)
        shop_obj = Shop.objects.filter(location=obj, active=True)
    except:
        obj = LocationDetails.objects.filter().last()
        shop_obj = Shop.objects.filter(location=obj, active=True)

    context = {
        'location':obj,
        'shop':shop_obj
    }

    return render(request, 'pages/contact.html', context)