from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog, name='blog'),
    path('post/<int:id>', views.single_post, name='single_post'),
    path('comment/<int:id>', views.comment, name='comment'),
    # path('post/comment/<int:id>/', views.comment, name='comment')

]