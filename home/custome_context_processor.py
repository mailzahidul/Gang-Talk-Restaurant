from .models import Company_info


def contact_us(request):
    try:
        obj = Company_info.objects.filter(active=True).last()
    except:
        obj = Company_info.objects.filter(active=True).last()
    context = {
        'contact': obj
    }
    return context
