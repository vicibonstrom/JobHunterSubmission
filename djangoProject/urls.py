"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from account import views as account_views  # Ensure to import your account views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jobs/', include('jobs.urls', namespace='jobs')),  # Include URLs for your jobs application
    path('accounts/login/', account_views.login_view, name='login'),  # Add this line for the login view
    path('accounts/', include('account.urls', namespace='account')),  # Include URLs for your account application
    path('accounts/', include('django.contrib.auth.urls')),  # Include Django's built-in auth URLs
    path('', include('core.urls', namespace='core')),  # Include URLs for your core application
]

from django.contrib import admin
from django.urls import path, include
from account import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jobs/', include('jobs.urls', namespace='jobs')),  # Include URLs for your jobs application
    path('accounts/login/', account_views.login_view, name='login'),  # Login view
    path('accounts/', include('account.urls', namespace='account')),  # Include URLs for your account application
    path('accounts/', include('django.contrib.auth.urls')),  # Include Django's built-in auth URLs
    path('', include('core.urls', namespace='core')),  # Include URLs for your core application
]

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jobs/', include('jobs.urls', namespace='jobs')),  # Include URLs for your jobs application
    path('accounts/login/', include('django.contrib.auth.urls')),  # Login view
    path('accounts/', include('account.urls', namespace='account')),  # Include URLs for your account application
    path('', lambda request: redirect('login')),  # Redirect the root URL to the login page
]
