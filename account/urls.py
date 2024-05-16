
from django.urls import path
from . import views

app_name = 'account'  # Add this line to define the app name

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),  # URL pattern for the logout view

]


