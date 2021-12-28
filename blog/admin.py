from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Categories)
admin.site.register(Tag)


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category','status']
    list_editable = ['status']

admin.site.register(Post, PostAdmin)
