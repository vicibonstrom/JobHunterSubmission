

from django.db import models
from django.contrib.auth.models import User

class JobCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)
    hours = models.CharField(max_length=50)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class JobImage(models.Model):
    job = models.ForeignKey(Job, related_name='images', on_delete=models.CASCADE)
    image_url = models.URLField()

    def __str__(self):
        return f"Image for {self.job.title}"
