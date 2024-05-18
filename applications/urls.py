from django.urls import path
from .views import JobApplicationWizard

app_name = 'applications'

urlpatterns = [
    path('<int:job_id>/', JobApplicationWizard.as_view(), name='apply_for_job'),
]

