from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages import success

# Create your views here.
def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            success(request, f'Account created for {username}')
            # form.save()
            return redirect('home')

    return render(request,'users/register.html', {'form': form, 'title': 'Register' } )
    
def login(request):
    return render(request,'users/login.html', {} )
    