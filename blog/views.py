from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponseRedirect
from django.db.models import Q

# Create your views here.

def blog(request):
    status = Status.objects.get(status='active')
    posts = Post.objects.filter(status=status)
    recent_posts = Post.objects.filter(status=status).order_by('-id')[:5]
    categories = Categories.objects.filter().order_by('-id')[:5]
    tags = Tag.objects.all().order_by('id')[:10]
    q = request.GET.get('search_word')
    posts = Post.objects.filter(status=status)
    if q is not None:
        search_p = posts.filter(
            Q(title__icontains=q) |
            Q(category__name__icontains=q) |
            Q(content__icontains=q)
            )
        if search_p:
            context = {
            'posts':search_p,
            'recent_posts':recent_posts,
            'categories':categories,
            'tags':tags
            }
            return render(request, 'pages/posts.html', context)
    context = {
        'posts':posts,
        'recent_posts':recent_posts,
        'categories':categories,
        'tags':tags
    }
    return render(request, 'pages/posts.html', context)


def category_posts(request, id):
    status = Status.objects.get(status='active')
    posts = Post.objects.filter(category=id)
    recent_posts = Post.objects.filter(status=status).order_by('-id')[:5]
    categories = Categories.objects.filter().order_by('-id')[:5]
    tags = Tag.objects.all().order_by('id')[:10]
    q = request.GET.get('search_word')
    posts = Post.objects.filter(status=status)
    if q is not None:
        search_p = posts.filter(
            Q(title__icontains=q) |
            Q(category__name__icontains=q) |
            Q(content__icontains=q)
            )
        if search_p:
            context = {
            'posts':search_p,
            'recent_posts':recent_posts,
            'categories':categories,
            'tags':tags
            }
            return render(request, 'pages/posts.html', context)
    context = {
        'posts':posts,
        'recent_posts':recent_posts,
        'categories':categories,
        'tags':tags
    }
    return render(request, 'pages/category_posts.html', context)


def single_post(request, id):
    post_obj = Post.objects.get(id=id)
    status = Status.objects.get(status='active')
    recent_posts = Post.objects.filter(status=status).order_by('-id')[:5]
    categories = Categories.objects.filter().order_by('-id')[:5]
    tags = Tag.objects.all().order_by('id')[:10]
    q = request.GET.get('search_word')
    posts = Post.objects.filter(status=status)
    if q is not None:
        search_p = posts.filter(
            Q(title__icontains=q) |
            Q(category__name__icontains=q) |
            Q(content__icontains=q)
            )
        if search_p:
            context = {
            'posts':search_p,
            'recent_posts':recent_posts,
            'categories':categories,
            'tags':tags
            }
            return render(request, 'pages/posts.html', context)
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