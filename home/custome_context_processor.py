from .models import Contact_us
from django.core.exceptions import MultipleObjectsReturned

def contact_us(request):
    try:
        obj = Contact_us.objects.get(active=True)
    except MultipleObjectsReturned:
        obj = Contact_us.objects.filter(active=True).last()
    context = {
        'contact':obj
    }
    return context