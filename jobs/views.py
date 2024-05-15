from django.shortcuts import render
# Create your views here.

jobs_options = [
    {'job_name': 'Cook', 'hours': 20},
    {'job_name': 'Cleaner', 'hours': 40}
]


def index(request):
    return render(request, 'jobs/index.html', context={
        'jobs_options': jobs_options
    })
