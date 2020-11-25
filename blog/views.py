from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Post, Comment
from .forms import CommentForm
from django.views.generic import (
    ListView, DetailView, 
    CreateView, UpdateView,
    DeleteView
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

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Post
    success_url = 'blog/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
     
def add_comment(request, id):
    post = get_object_or_404(Post, pk=id)
    form = CommentForm(request.POST | None)
    if form.is_valid():
        comment = form.save()
        comment.post = post
        comment.author = request.user
        comment.save()
        return redirect('home')
    return render(request, 'blog/home.html', {'form': form})


def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'blog/about.html', context)
# def post_detail(request, id):
#     # post = get_object_or_404(Post, pk=id)
#     post = Post.objects.get(pk=id)
#     comments = Comment.objects.get(post=post)
#     return render(request, 'blog/post_detail.html',{'post': post, 'comments': comments})