from django.shortcuts import render

# Create your views here.
posts = [
    {
        'author': 'CoreyMs',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2020',
    }, 
    {
        'author': 'Jane doe',
        'title': 'Blog Post 1',
        'content': 'Second post content',
        'date_posted': 'August 28, 2020',
    }, 
]

def home(request):
    context = {
        'title': 'Home',
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'blog/about.html', context)