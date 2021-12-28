from .models import CompanyInfo


def contact_us(request):
    try:
        obj = CompanyInfo.objects.filter(active=True).last()
    except:
        obj = CompanyInfo.objects.filter(active=True).last()
    context = {
        'contact': obj
    }
    return context
