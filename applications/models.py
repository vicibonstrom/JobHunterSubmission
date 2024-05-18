from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from jobs.models import Job
from django_countries.fields import CountryField

class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    street_name = models.CharField(max_length=255)
    house_number = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    country = CountryField()
    postal_code = models.CharField(max_length=20)
    cover_letter = models.TextField()
    review = models.TextField(default='')
    date_applied = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.job.title}'
