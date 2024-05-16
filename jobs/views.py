from django.shortcuts import render
from .models import Job
from django.contrib.auth.decorators import login_required

@login_required
def list_jobs(request):
    jobs = Job.objects.filter(is_available=True)  # Only show available jobs
    return render(request, 'job_list.html', {'jobs': jobs})

from django.shortcuts import render
from .models import Job

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})


from django.shortcuts import render, redirect, get_object_or_404
from .forms import JobForm, JobCategoryForm, JobImageForm

def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jobs:index')
    else:
        form = JobForm()
    return render(request, 'jobs/add_job.html', {'form': form})

def add_category(request):
    if request.method == 'POST':
        form = JobCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jobs:add_job')
    else:
        form = JobCategoryForm()
    return render(request, 'jobs/add_category.html', {'form': form})

def add_image(request):
    if request.method == 'POST':
        form = JobImageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jobs:add_job')
    else:
        form = JobImageForm()
    return render(request, 'jobs/add_image.html', {'form': form})

def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'jobs/job_detail.html', {'job': job})
