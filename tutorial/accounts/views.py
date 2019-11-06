from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash # This is used so that the user is still loggged in after password change
from django.contrib.auth.forms import (
    UserCreationForm, 
    UserChangeForm, 
    PasswordChangeForm,
)

from .forms import (
    RegistrationForm, 
    EditProfileForm,
)


# Create your views here.
def login_redirect(request):
    # return redirect('/accounts/login')
    return redirect(reverse('accounts:login'))

def register(request):

    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect(reverse('home:home'))
    else:
        form = RegistrationForm()


    context = {
        'title' : 'Register Page',
        'form' : form,
    }
    template_name = 'accounts/register.html'
    return render(request,template_name,context)


@login_required
def view_profile(request):

    context = {
        'title' : 'Profile',
        'user' : request.user,
    }
    template_name = 'accounts/profile.html'
    return render(request, template_name, context)


@login_required
def edit_profile(request):
    if request.method=='POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('accounts:view_profile')

    else:
        form = EditProfileForm(instance=request.user)


    context = {
        'title' : 'Edit Profile',
        'form' : form,
    }
    template_name = 'accounts/edit_profile.html'
    return render(request, template_name, context)


@login_required
def change_password(request):
    if request.method=='POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('accounts:view_profile')
        else:
            return redirect('accounts:change-password')

    else:
        form = PasswordChangeForm(user=request.user)


    context = {
        'title' : 'Edit Password',
        'form' : form,
    }
    template_name = 'accounts/change_password.html'
    return render(request, template_name, context)