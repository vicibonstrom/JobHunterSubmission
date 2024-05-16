
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            user = form.save()
            print(user)
            login(request, user)  # Log the user in after registration
            return redirect('index')  # Redirect to the home page after registration
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('jobs:index')  # Redirect to the jobs page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form': form})
