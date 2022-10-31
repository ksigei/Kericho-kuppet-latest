import re
from django.shortcuts import render,get_object_or_404
from django.contrib import messages
from .forms import CommentForm
from .models import Post, Comment
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# def home(request):
#     return render(request, 'home.html')

def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")

    context = {"posts": posts,

               }
    return render(request, "blog_index.html", context)


def pagination(posts,request):
    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 2)
    try:
        entries = paginator.page(page)
    except PageNotAnInteger:
        entries = paginator.page(1)
    except EmptyPage:
        entries = paginator.page(paginator.num_pages)
    return entries


def blog_list(request):
    posts = Post.objects.all().order_by("-created_on")

    context = { "entries":pagination(posts,request)}
    return render(request, "blog_index.html",  context )

def blog_category(request, category):
    
    posts = Post.objects.filter(categories__name__contains=category).order_by(
        "-created_on"
    )
    context = {"category": category, "entries":pagination(posts,request)  }
    return render(request, "blog_index.html", context)

def blog_tag(request, tag):
    
    posts = Post.objects.filter(tags__slug=tag).order_by(
        "-created_on"
    )

    context = {"tag": tag, "entries": pagination(posts,request) }
    return render(request, "blog_index.html",context)


def blog_detail(request, slug):
    
    post = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.filter(post=post)

    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            form = CommentForm()
        else:
            messages.warning(request, 'Oops comment was not posted!')
    context = {"post": post, "comments": comments,  "form": form}
    return render (request, "blog_detail.html", context)

def about(request):
    return render (request, "about.html")
from django.shortcuts import render,get_object_or_404
from django.contrib import messages
from .forms import CommentForm
from .models import Post, Comment
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



# def blog_index(request):
#     posts = Post.objects.all().order_by("-created_on")

#     context = {"posts": posts,

#                }
#     return render(request, "home.html", context)


def pagination(posts,request):
    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 2)
    try:
        entries = paginator.page(page)
    except PageNotAnInteger:
        entries = paginator.page(1)
    except EmptyPage:
        entries = paginator.page(paginator.num_pages)
    return entries


def blog_list(request):
    posts = Post.objects.all().order_by("-created_on")

    context = { "entries":pagination(posts,request)}
    return render(request, "blog_index.html",  context )

def blog_category(request, category):
    
    posts = Post.objects.filter(categories__name__contains=category).order_by(
        "-created_on"
    )
    context = {"category": category, "entries":pagination(posts,request)  }
    return render(request, "blog_index.html", context)

def blog_tag(request, tag):
    
    posts = Post.objects.filter(tags__slug=tag).order_by(
        "-created_on"
    )

    context = {"tag": tag, "entries": pagination(posts,request) }
    return render(request, "blog_index.html",context)


def blog_detail(request, slug):
    
    post = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.filter(post=post)

    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            form = CommentForm()
        else:
            messages.warning(request, 'Oops comment was not posted!')
    context = {"post": post, "comments": comments,  "form": form}
    return render (request, "blog_detail.html", context)

def about(request):
    return render (request, "about.html")
