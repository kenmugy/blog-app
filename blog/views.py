from django.shortcuts import render
from .models import Post
from django.views.generic import ListView



def home(request):
    posts = Post.objects.all()
    context = {
        'title': 'Home',
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = 'posts'


def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'blog/about.html', context)