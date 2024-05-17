from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Job, JobApplication
from .forms import JobForm, JobCategoryForm, JobImageForm, JobApplicationForm

@login_required
def job_list(request):
    jobs = Job.objects.filter(is_available=True)  # Only show available jobs
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

@login_required
def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jobs:job_list')  # Redirect to the job list page
    else:
        form = JobForm()
    return render(request, 'jobs/add_job.html', {'form': form})

@login_required
def add_category(request):
    if request.method == 'POST':
        form = JobCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jobs:add_job')
    else:
        form = JobCategoryForm()
    return render(request, 'jobs/add_category.html', {'form': form})

@login_required
def add_image(request):
    if request.method == 'POST':
        form = JobImageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jobs:add_job')
    else:
        form = JobImageForm()
    return render(request, 'jobs/add_image.html', {'form': form})

@login_required
def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'jobs/job_detail.html', {'job': job})


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Job, JobApplication
from .forms import JobApplicationForm
from django.urls import reverse

@login_required
def apply_for_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.user = request.user
            application.save()
            return redirect('jobs:application_success')
    else:
        form = JobApplicationForm()
    return render(request, 'jobs/apply_for_job.html', {'form': form, 'job': job})

def application_success(request):
    return render(request, 'jobs/application_success.html')
