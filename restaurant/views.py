from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.db.models import Prefetch
from home.models import Brand
from django.core.mail import send_mail
# Create your views here.

def offers(request):
    product_tabs = Product_tab.objects.all()
    context = {
        'pro_tab':product_tabs
        }
    return render(request, 'pages/offers.html', context)



def food_details(request, id):
    product = Product.objects.get(id=id)
    if product.discount:
        discount_price = product.price - product.discount
        context = {
            'product':product,
            'discount_price':discount_price
        }
        return render(request, 'pages/food_details.html', context)
    context = {
        'product':product
    }
    return render(request, 'pages/food_details.html', context)


def reservation(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        address=request.POST['address']
        phone=request.POST['phone']
        num_table=request.POST['num_table']
        num_people=request.POST['num_people']
        date=request.POST['date']
        time=request.POST['time']

        subject = "Gang Talk Cafe Reservation"
        sender = "demo@gmail.com"
        message = "I am "+name+". I want to reserver your restaurent on "+date+""
        try:
            obj = Reservation.objects.create(name=name, email=email, address=address, phone=phone, num_of_table=num_table, num_of_people=num_people, date=date, time=time)
            msg_mail = str(message)+" " + str(sender)
            send_mail(subject , msg_mail, sender ,  ['mailzahidul@gmail.com'], fail_silently=False)
            messages.success(request, "Your Reservation Submitted Successfully...")
        except:
            messages.error(request, "Your Reservation not send, Please call or try again")
    return render(request, 'pages/reservation.html')




def menu(request):
    objs = Meal_category.objects.all().order_by('id')
    brands = Brand.objects.all().order_by('-id')[:10]
    context = {
        'categories':objs,
        'brands':brands
    }
    return render(request, 'pages/menu.html', context)


def catering(request):
    products = Product.objects.filter(is_catering=True, is_active=True)
    context = {
        'products':products
        }
    return render(request, 'pages/catering.html', context)
    

def catering_details(request, id):
    product = Product.objects.get(id=id)
    if product.discount:
        discount_price = product.price - product.discount
        context = {
            'product':product,
            'discount_price':discount_price
        }
        return render(request, 'pages/catering_details.html', context)
    context = {
    'product':product
    }
    return render(request, 'pages/catering_details.html', context)


def catering_mail(request):
    if request.method == 'POST':
        name = request.POST['name']
        sku = request.POST['sku']
        quantity = request.POST['quantity']
        subject = "Gang Talk Cafe Product Intereste"
        sender = "demo@gmail.com"
        message = "I am interested to "+name+" whose sku code is "+sku
        try:
            msg_mail = str(message)+" " + str(sender)
            send_mail(subject , msg_mail, sender ,  ['mailzahidul@gmail.com'], fail_silently=False)
            messages.success(request, 'Mail Submit Successfully...')
        except Exception as err:
            print(err, "Mail submission failed")
    return redirect('catering')


def custome_order(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        address=request.POST['address']
        phone=request.POST['phone']
        pl_num=request.POST['pl_num']
        datetime=request.POST['datetime']
        description=request.POST['description']
        
        subject = "Gang Talk Cafe Custom Order"
        sender = "demo@gmail.com"
        try:
            obj = Custom_order.objects.create(name=name, email=email, address=address, phone=phone, num_of_people=pl_num, date_time=datetime, description=description)
            msg_mail = str(description)+" " + str(sender)
            send_mail(subject , msg_mail, sender ,  ['mailzahidul@gmail.com'], fail_silently=False)
            messages.success(request, "Your Custome order Submitted Successfully...")
        except Exception as err:
            messages.error(request, 'Your order not send')
    return render(request, 'pages/custom_menu_form.html')