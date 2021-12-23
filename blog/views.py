from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def blog(request):
    posts = Post.objects.filter(status='published')
    recent_posts = Post.objects.filter(status='published').order_by('-id')[:5]
    categories = Categories.objects.filter().order_by('-id')[:5]
    tags = Tag.objects.all().order_by('id')[:10]
    # posts_list = Post.objects.filter(status='published')
    page = request.GET.get('page', 10)
    paginator = Paginator(posts, 10)
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)

    q = request.GET.get('search_word')
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
            'tags':tags,
            'pagi':post
            }
            return render(request, 'pages/posts.html', context)
        else:
            messages.warning(request, "There is no post with your search keywod")
    context = {
        'posts':posts,
        'recent_posts':recent_posts,
        'categories':categories,
        'tags':tags,
        'pagi':post
    }
    return render(request, 'pages/posts.html', context)


def category_posts(request, id):
    posts = Post.objects.filter(status='published', category=id)
    if not posts:
        messages.warning(request, "There is no posts in this category")

    recent_posts = Post.objects.filter(status='published').order_by('-id')[:5]
    categories = Categories.objects.filter().order_by('-id')[:5]
    tags = Tag.objects.all().order_by('id')[:10]

    page = request.GET.get('page', 10)
    paginator = Paginator(posts, 10)
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)

    q = request.GET.get('search_word')
    if q is not None:
        posts = Post.objects.filter(status='published')
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
            'tags':tags,
            'pagi':post
            }
            return render(request, 'pages/category_posts.html', context)
        else:
            messages.warning(request, "There is no post with your search keywod")
        
    context = {
        'posts':posts,
        'recent_posts':recent_posts,
        'categories':categories,
        'tags':tags,
        'pagi':post
    }
    return render(request, 'pages/category_posts.html', context)


def tag_posts(request, id):
    posts = Post.objects.filter(status='published', tags = id)
    if not posts:
        messages.warning(request, "There is no posts in this tags")
    recent_posts = Post.objects.filter(status='published').order_by('-id')[:5]
    categories = Categories.objects.filter().order_by('-id')[:5]
    tags = Tag.objects.all().order_by('id')[:10]

    page = request.GET.get('page', 10)
    paginator = Paginator(posts, 10)
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)

    q = request.GET.get('search_word')
    if q is not None:
        posts = Post.objects.filter(status='published')
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
            'tags':tags,
            'pagi':post
            }
            return render(request, 'pages/category_posts.html', context)
        else:
            messages.warning(request, "There is no post with your search keywod")


    context = {
            'posts':posts,
            'recent_posts':recent_posts,
            'categories':categories,
            'tags':tags
    }
    return render(request, 'pages/posts.html', context)


def single_post(request, id):
    post_obj = Post.objects.get(id=id)
    recent_posts = Post.objects.filter(status='published').order_by('-id')[:5]
    categories = Categories.objects.filter().order_by('-id')[:5]
    tags = Tag.objects.all().order_by('id')[:10]
    q = request.GET.get('search_word')
    posts = Post.objects.filter(status='published')
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
        else:
            messages.warning(request, "There is no post with your search keywod")

    context = {
        'post':post_obj,
        'recent_posts':recent_posts,
        'categories':categories
    }
    return render(request, 'pages/single_post.html', context)
