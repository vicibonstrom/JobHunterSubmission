
from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('', views.job_list, name='index'),
    path('add/', views.add_job, name='add_job'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_image/', views.add_image, name='add_image'),
    path('<int:pk>/', views.job_detail, name='job_detail'),
    path('add/', views.add_job, name='add_job'),
    path('<int:pk>/apply/', views.apply_for_job, name='apply_for_job'),
]



app_name = 'jobs'

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('<int:pk>/', views.job_detail, name='job_detail'),
    path('add/', views.add_job, name='add_job'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_image/', views.add_image, name='add_image'),
    path('<int:pk>/apply/', views.apply_for_job, name='apply_for_job'),
    path('application_success/', views.application_success, name='application_success'),

]
