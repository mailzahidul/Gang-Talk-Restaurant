from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Designation)
admin.site.register(Status)
admin.site.register(Categories)
admin.site.register(Tag)
admin.site.register(Comment)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'designation', 'status']
    list_editable = ['status']

admin.site.register(Author, AuthorAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'is_featured', 'is_active']
    list_editable = ['status','is_featured', 'is_active']

admin.site.register(Post, PostAdmin)