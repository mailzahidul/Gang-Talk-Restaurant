from django.contrib import admin
from .models import *


class Contact_usAdmin(admin.ModelAdmin):
    list_display = ['shop_address', 'phone', 'email', 'active']
    list_editable = ['active']

admin.site.register(Contact_us, Contact_usAdmin)

class LocationAdmin(admin.ModelAdmin):
    list_display = ['title', 'active']
    list_editable = ['active']

admin.site.register(LocationDetails, LocationAdmin)

class ShopAdmin(admin.ModelAdmin):
    list_display = ['shop', 'district', 'phone', 'active']
    list_editable = ['active']

admin.site.register(Shop, ShopAdmin)