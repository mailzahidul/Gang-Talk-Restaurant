from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Food_category)

class OfferAdmin(admin.ModelAdmin):
    list_display=['offer_name', 'is_active']
    list_editable=['is_active']

admin.site.register(Offer, OfferAdmin)

admin.site.register(Product_for)
admin.site.register(Product_tab)


class ProductAdmin(admin.ModelAdmin):
    list_display=['name', 'sku', 'price', 'discount', 'get_categories', 'quantity', 'product_tab', 'is_stock']
    list_editable=['is_stock']

    def get_categories(self, obj):
        return ", ".join([p.name for p in obj.category.all()])


admin.site.register(Product, ProductAdmin)
