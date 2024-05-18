from django.shortcuts import get_object_or_404, redirect
from formtools.wizard.views import SessionWizardView
from .forms import ContactInformationForm, CoverLetterForm, ExperienceForm, RecommendationForm
from jobs.models import Job
from .models import JobApplication

FORMS = [
    ("contact_information", ContactInformationForm),
    ("cover_letter", CoverLetterForm),
    ("experience", ExperienceForm),
    ("recommendation", RecommendationForm),
]

TEMPLATES = {
    "contact_information": "applications/contact_information.html",
    "cover_letter": "applications/cover_letter.html",
    "experience": "applications/experience.html",
    "recommendation": "applications/recommendation.html",
}

class JobApplicationWizard(SessionWizardView):
    form_list = FORMS

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        job = get_object_or_404(Job, pk=self.kwargs['job_id'])
        application = JobApplication(job=job, user=self.request.user)

        for form in form_list:
            if isinstance(form, ExperienceForm) or isinstance(form, RecommendationForm):
                continue
            for field, value in form.cleaned_data.items():
                setattr(application, field, value)

        application.save()

        for form in form_list:
            if isinstance(form, ExperienceForm):
                for experience in form:
                    # Save each experience related to the application
                    experience_instance = experience.save(commit=False)
                    experience_instance.application = application
                    experience_instance.save()
            if isinstance(form, RecommendationForm):
                for recommendation in form:
                    # Save each recommendation related to the application
                    recommendation_instance = recommendation.save(commit=False)
                    recommendation_instance.application = application
                    recommendation_instance.save()

        return redirect('jobs:application_success')
