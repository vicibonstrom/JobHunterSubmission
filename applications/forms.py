from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

class ContactInformationForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    street_name = forms.CharField(max_length=100)
    house_number = forms.CharField(max_length=10)
    city = forms.CharField(max_length=100)
    country = CountryField().formfield(widget=CountrySelectWidget())
    postal_code = forms.CharField(max_length=20)

class CoverLetterForm(forms.Form):
    cover_letter = forms.CharField(widget=forms.Textarea)

class ExperienceForm(forms.Form):
    place_of_work = forms.CharField(max_length=100)
    role = forms.CharField(max_length=100)
    start_date = forms.DateField(widget=forms.SelectDateWidget(years=range(1980, 2025)))
    end_date = forms.DateField(widget=forms.SelectDateWidget(years=range(1980, 2025)))

class RecommendationForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=20)
    may_be_contacted = forms.BooleanField(required=False)
    role = forms.CharField(max_length=100)

class ReviewForm(forms.Form):
    pass

class ConfirmationForm(forms.Form):
    pass
