from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class JobCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)
    hours = models.CharField(max_length=50)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    is_available = models.BooleanField(default=True)
    company = models.CharField(max_length=200, default='Unknown Company')
    due_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title


class JobImage(models.Model):
    job = models.ForeignKey(Job, related_name='images', on_delete=models.CASCADE)
    image_url = models.URLField()

    def __str__(self):
        return f"Image for {self.job.title}"

