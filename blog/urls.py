from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog, name='blog'),
    path('post/<int:id>', views.single_post, name='single_post'),
    path('category_posts/<int:id>', views.category_posts, name='category_posts'),
    path('tags/<int:id>', views.tag_posts, name='tag_posts')

]