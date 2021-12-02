from django.shortcuts import render

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
    return render(request, 'pages/contact.html')
