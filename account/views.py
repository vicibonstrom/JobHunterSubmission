from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request, 'account/index.html')

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
                return redirect('index')  # Redirect to the home page after login
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})
