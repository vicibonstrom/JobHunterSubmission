
from .forms import JobForm
from .models import JobCategory, JobImage
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from .models import Job, JobCategory


def job_list(request):
    categories = JobCategory.objects.all()
    jobs = Job.objects.all()

    category_id = request.GET.get('category')
    company_name = request.GET.get('company')
    search_query = request.GET.get('search')

    if category_id:
        jobs = jobs.filter(category_id=category_id)

    if company_name:
        jobs = jobs.filter(company__icontains=company_name)

    if search_query:
        jobs = jobs.filter(title__icontains=search_query)

    order_by = request.GET.get('order_by')
    if order_by in ['date', 'due_date']:
        jobs = jobs.order_by(order_by)

    categories = JobCategory.objects.all()
    return render(request, 'jobs/job_list.html', {
        'jobs': jobs,
        'categories': categories,
    })



    if category:
        jobs = jobs.filter(category__name=category)
    if company:
        jobs = jobs.filter(company=company)
    if applied:
        jobs = jobs.filter(applications__user=request.user)

    # Sorting
    order_by = request.GET.get('order_by')
    if order_by in ['date', 'due_date']:
        jobs = jobs.order_by(order_by)

    categories = JobCategory.objects.all()
    return render(request, 'jobs/job_list.html', {
        'jobs': jobs,
        'categories': categories,
    })
@login_required


def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save(user=request.user)
            return redirect('jobs:job_list')
    else:
        form = JobForm()
    return render(request, 'jobs/add_job.html', {'form': form})

@login_required
def add_category(request):
    if request.method == 'POST':
        form = JobCategory(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jobs:add_job')
    else:
        form = JobCategory()
    return render(request, 'jobs/add_category.html', {'form': form})

@login_required
def add_image(request):
    if request.method == 'POST':
        form = JobImage(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jobs:add_job')
    else:
        form = JobImage()
    return render(request, 'jobs/add_image.html', {'form': form})

@login_required
def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'jobs/job_detail.html', {'job': job})


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Job, JobApplication
from .forms import JobForm
from django.urls import reverse

@login_required
def apply_for_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.user = request.user
            application.save()
            return redirect('jobs:application_success')
    else:
        form = JobForm()
    return render(request, 'jobs/apply_for_job.html', {'form': form, 'job': job})

def application_success(request):
    return render(request, 'jobs/application_success.html')

