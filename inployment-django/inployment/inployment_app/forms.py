from django import forms

class BusinessForm(forms.Form):
    business_name = forms.CharField(
        max_length=100,
        label='Company Name',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    business_email = forms.EmailField(
        required=True,
        label='Email address',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

class CandidateForm(forms.Form):
    candidate_email = forms.EmailField(
        required=True,
        label='Email address',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

class InterestedForm(forms.Form):
    interested_email = forms.EmailField(
        required=True,
        label='Email address',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
