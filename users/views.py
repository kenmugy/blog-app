from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.messages import success
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    form = UserRegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            success(request, f'Account created for {username}, Login to continue..')
            form.save()
            return redirect('login')

    return render(request,'users/register.html', {'form': form, 'title': 'Register' } )

@login_required    
def profile(request):
    return render(request,'users/profile.html', {} )
    