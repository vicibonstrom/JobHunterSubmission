from django.contrib import admin
from .models import JobCategory
from .models import JobImage
from .models import Job
# Register your models here.

admin.site.register(JobCategory)
admin.site.register(JobImage)
admin.site.register(Job)
