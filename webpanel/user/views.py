from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import UserProfileUpdateForm, UserUpdateForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

@login_required
def ProfileUpdate(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user, prefix='user')
        userprofile_form = UserProfileUpdateForm(request.POST, instance=request.user.profile, prefix='userprofile')

        if user_form.is_valid() * userprofile_form.is_valid():
            user = user_form.save()
            userprofile = userprofile_form.save(commit=False)
            userprofile.user = user
            userprofile.save()
            return render(request, 'user/profile/update.html', {'user_form': user_form, 'userprofile_form': userprofile_form,'saved': True})

    user_form = UserUpdateForm(instance=request.user, prefix='user')
    userprofile_form = UserProfileUpdateForm(instance=request.user.profile, prefix='userprofile')
    return render(request, 'user/profile/update.html', {'user_form': user_form, 'userprofile_form': userprofile_form, 'saved': False})

def SignUp(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
       user = form.save()
       login(request, user)
       return redirect('user:ProfileUpdate')
    
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
