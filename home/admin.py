from django.contrib import admin
from .models import *


class Contact_usAdmin(admin.ModelAdmin):
    list_display = ['shop_address', 'phone', 'email', 'active']
    list_editable = ['active']

admin.site.register(Contact_us, Contact_usAdmin)



admin.site.register(LocationDetails)
admin.site.register(Shop)