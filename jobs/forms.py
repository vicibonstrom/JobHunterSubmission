from django import forms
from .models import Job, JobCategory, JobImage, JobApplication

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'category', 'hours', 'posted_by']

class JobCategoryForm(forms.ModelForm):
    class Meta:
        model = JobCategory
        fields = ['name']

class JobImageForm(forms.ModelForm):
    class Meta:
        model = JobImage
        fields = ['job', 'image_url']

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['cover_letter', 'resume']
