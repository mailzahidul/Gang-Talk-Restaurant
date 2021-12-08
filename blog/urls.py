from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog, name='blog'),
    path('post/<int:id>', views.single_post, name='single_post'),
    path('comment/<int:id>', views.comment, name='comment'),
    path('category_posts/<int:id>', views.category_posts, name='category_posts'),
    # path('search_view/', views.search_view, name="search_view")
    # path('post/comment/<int:id>/', views.comment, name='comment')

]