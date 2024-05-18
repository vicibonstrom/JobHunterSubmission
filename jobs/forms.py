from django import forms
from .models import Job, JobCategory

class JobForm(forms.ModelForm):
    new_category = forms.CharField(max_length=100, required=False, help_text="Leave blank if not adding a new category")

    class Meta:
        model = Job
        fields = ['title', 'description', 'category', 'hours', 'company', 'due_date', 'is_available']


    def clean(self):
        cleaned_data = super().clean()
        new_category_name = cleaned_data.get('new_category')
        category = cleaned_data.get('category')

        if not new_category_name and not category:
            raise forms.ValidationError('Please select an existing category or enter a new one.')

        return cleaned_data

    def save(self, commit=True, user=None):
        new_category_name = self.cleaned_data.get('new_category')
        if new_category_name:
            category, created = JobCategory.objects.get_or_create(name=new_category_name)
            self.instance.category = category
        if user:
            self.instance.posted_by = user
        return super().save(commit)
