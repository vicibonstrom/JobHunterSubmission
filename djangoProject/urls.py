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
from jobs import views as job_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('account.urls', namespace='account')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('jobs/', include('jobs.urls', namespace='jobs')),
    path('', job_views.job_list, name='home'),
]


from django.contrib import admin
from django.urls import path, include
from jobs import views as job_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('account.urls', namespace='account')),
    path('jobs/', include('jobs.urls', namespace='jobs')),
    path('', job_views.job_list, name='home'),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('account.urls', namespace='account')),
    path('jobs/', include('jobs.urls', namespace='jobs')),
    path('', job_views.job_list, name='home'),
    path('apply/', include('applications.urls', namespace='applications')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
