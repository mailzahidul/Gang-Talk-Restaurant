from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Categories)
admin.site.register(Tag)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'author_status']
    list_editable = ['author_status']

admin.site.register(Author, AuthorAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category','status']
    list_editable = ['status']

admin.site.register(Post, PostAdmin)