from django import forms

class BusinessForm(forms.Form):
    business_name = forms.CharField(
        max_length=100,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Business name',
                                      'class': 'form-control'})
    )
    business_email = forms.EmailField(
        required=True,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Email address',
                                      'class': 'form-control'})
    )

class CandidateForm(forms.Form):
    candidate_email = forms.EmailField(
        required=True,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Email address',
                                      'class': 'form-control'})
    )

class InterestedForm(forms.Form):
    interested_email = forms.EmailField(
        required=True,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Email address',
                                      'class': 'form-control'})
    )
