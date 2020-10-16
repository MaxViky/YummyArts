from django.contrib.auth import login, authenticate
from django.contrib.auth.context_processors import auth
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib import auth
from .forms import *


def LogIn(request):
    invalid = 'Invalid login or password'
    if request.method == 'POST':
        form = loginForm(request.POST)
        if 'LogIn' in request.POST:
            if form.is_valid():
                cd = form.cleaned_data
                user = authenticate(username=cd['username'], password=cd['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect("/")
                    else:
                        return render(request, 'LoginForm.html', {'log_form': form, 'invalid': invalid})
                else:
                    return render(request, 'LoginForm.html', {'log_form': form, 'invalid': invalid})
    else:
        form = loginForm()
    return render(request, 'LoginForm.html', {'log_form': form})


def LogOut(request):
    auth.logout(request)
    return redirect("/")


def register(request):
    if request.method == 'POST':
        user_form = regForms(request.POST)
        if 'regbut' in request.POST:
            if user_form.is_valid():
                new_user = user_form.save(commit=False)
                new_user.set_password(user_form.cleaned_data['password2'])
                new_user.save()
                return redirect("/")
    else:
        user_form = regForms()
    return render(request, 'RegistrationForm.html', {'reg_form': user_form})


def profile(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'Profile.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
        return render(request, 'Profile.html', {'form': form})
