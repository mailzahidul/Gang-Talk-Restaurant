from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect

# Create your views here.

def blog(request):
    status = Status.objects.get(status='active')
    posts = Post.objects.filter(is_active=True, status=status)
    recent_posts = Post.objects.filter(is_active=True).order_by('-id')[:5]
    categories = Categories.objects.filter().order_by('-id')[:5]
    context = {
        'posts':posts,
        'recent_posts':recent_posts,
        'categories':categories
    }
    return render(request, 'pages/posts.html', context)


def single_post(request, id):
    post_obj = Post.objects.get(id=id)
    recent_posts = Post.objects.filter(is_active=True).order_by('-id')[:5]
    categories = Categories.objects.filter().order_by('-id')[:5]
    context = {
        'post':post_obj,
        'recent_posts':recent_posts,
        'categories':categories
    }
    return render(request, 'pages/single_post.html', context)

def comment(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        print(name, email, message, "CHECK")
        Comment.objects.create(post=post, name=name, email=email, message=message)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))