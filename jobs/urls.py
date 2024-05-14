from django.urls import path

from jobs import (views)

urlpatterns = [
    # http://localhost:8000/hunters
    path('', views.index, name="jobs-index"),
]
