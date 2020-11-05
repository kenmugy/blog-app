from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.messages import success
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

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
    u_form = UserUpdateForm(request.POST or None,instance=request.user)
    p_form = ProfileUpdateForm(request.POST or None, request.FILES or None,instance=request.user.profile)

    if u_form.is_valid() and p_form.is_valid():
        u_form.save()
        p_form.save()
        success(request, f'Account Updated..')
        return redirect('profile')

    context = {
        'u_form':u_form,
        'p_form': p_form
    }
    return render(request,'users/profile.html', context )
    