from django.shortcuts import render
from .models import *
# Create your views here.

def offers(request):
    pro_tab = Product_tab.objects.all()
    offers = Offer.objects.filter(is_active=False)
    print(offers, "CHECK")
    context = {
        'pro_tab':pro_tab,
        'offers':offers,

    }
    return render(request, 'pages/offers.html', context)