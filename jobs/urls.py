

from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('add/', views.add_job, name='add_job'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_image/', views.add_image, name='add_image'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
]
