from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Category)


class Custom_orderAdmin(admin.ModelAdmin):
    list_display=['name', 'phone', 'email','date_time', 'is_response']
    list_editable= ['is_response']
    readonly_fields = ['name', 'email', 'address','phone', 'num_of_people','date_time', 'description']

admin.site.register(Custom_order, Custom_orderAdmin)

class OfferAdmin(admin.ModelAdmin):
    list_display=['offer_name', 'is_active']
    list_editable=['is_active']

admin.site.register(Offer, OfferAdmin)


admin.site.register(Product_tab)
admin.site.register(Meal_category)


class ProductAdmin(admin.ModelAdmin):
    list_display=['name', 'sku', 'price', 'discount', 'get_categories','is_active']
    list_editable=['is_active']

    def get_categories(self, obj):
        return ", ".join([p.name for p in obj.category.all()])
    
    


admin.site.register(Product, ProductAdmin)


class ReservationAdmin(admin.ModelAdmin):
    list_display=['name', 'phone', 'date', 'time', 'is_response']
    list_editable= ['is_response']
    readonly_fields = ['name', 'email', 'address','phone', 'num_of_table', 'num_of_people','date', 'time']

admin.site.register(Reservation, ReservationAdmin)


# This Section for Menu 

admin.site.register(Item)
