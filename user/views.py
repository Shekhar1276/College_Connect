# user/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm, SignInForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Change 'home' to the name of your home view
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = SignInForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Change 'home' to the name of your home view
    else:
        form = SignInForm()
    return render(request, 'signin.html', {'form': form})

from django.contrib.auth import logout

def signout(request):
    logout(request)
    return redirect('home')  # Redirect to the home page or any other desired page
