from django.contrib import admin
from .models import *
from django.utils.html import format_html


class Company_infoAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="30" height="30" />'.format(obj.logo.url))
    
    image_tag.short_description = 'Logo Preview'
    readonly_fields = ['image_tag']
    list_display = ['name', 'image_tag']
    list_display = ['name', 'image_tag','phone', 'email', 'active']
    list_editable = ['active']

admin.site.register(Company_info, Company_infoAdmin)




class ShopAdmin(admin.ModelAdmin):
    list_display = ['shop_title', 'district', 'phone', 'active']
    list_editable = ['active']

admin.site.register(Shop, ShopAdmin)



admin.site.register(About_us)




class HistoryAdmin(admin.ModelAdmin):
    list_display= ['happy_customer', 'avail_food_item', 'running_order']

admin.site.register(History, HistoryAdmin)




admin.site.register(Subscribtion)


class BrandAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="60" height="60" />'.format(obj.logo.url))
    
    image_tag.short_description = 'Image Preview'
    readonly_fields = ['image_tag']
    list_display = ['name', 'image_tag']

admin.site.register(Brand, BrandAdmin)

# admin.site.register(Gallery)


class FeatureAdmin(admin.ModelAdmin):
    list_display= ['title', 'is_active']
    list_editable= ['is_active']

admin.site.register(Feature, FeatureAdmin)




class Feature_itemsAdmin(admin.ModelAdmin):
    list_display= ['title']

admin.site.register(Feature_items, Feature_itemsAdmin)





admin.site.register(Gang_talk)




class SliderAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="20" height="20" />'.format(obj.image.url))
    
    image_tag.short_description = 'Image Preview'
    readonly_fields = ['image_tag']

    list_display=['title', 'image_tag','discount_percent']    

admin.site.register(Slider, SliderAdmin)





class MealtimeAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="20" height="20" />'.format(obj.image.url))
    
    image_tag.short_description = 'Image Preview'
    readonly_fields = ['image_tag']

    list_display=['name', 'duration','image_tag']

admin.site.register(Meal_time, MealtimeAdmin)