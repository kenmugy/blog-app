from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from django.views.generic import (
    ListView, DetailView, 
    CreateView
)



def home(request):
    posts = Post.objects.all()
    context = {
        'title': 'Home',
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    ordering = '-date_posted'
    template_name = "blog/home.html"
    context_object_name = 'posts'

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        

def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'blog/about.html', context)