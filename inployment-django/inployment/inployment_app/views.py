from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Test view from Django tutorial: https://docs.djangoproject.com/en/1.9/intro/tutorial01/

def index(request):
    # Save email
    business_form = BusinessForm()
    candidate_form = CandidateForm()
    interested_form = InterestedForm()

    if request.method == 'POST':
        if 'business' in request.POST:
            business_form = BusinessForm(request.POST)
            if business_form.is_valid():
                business_name = business_form.cleaned_data['business_name']
                business_email = business_form.cleaned_data['business_email']
                Business.objects.create(name=business_name,
                                        email_address=business_email)
                return redirect('thanks/')

        elif 'candidate' in request.POST:
            candidate_form = CandidateForm(request.POST)
            if candidate_form.is_valid():
                candidate_email = candidate_form.cleaned_data['candidate_email']
                Candidate.objects.create(email_address=candidate_email)
                return redirect('thanks/')

        elif 'interested' in request.POST:
            interested_form = InterestedForm(request.POST)
            if interested_form.is_valid():
                interested_email = interested_form.cleaned_data['interested_email']
                Candidate.objects.create(email_address=interested_email)
                return redirect('thanks/')

    return render(request, 'home.html', {'business_form': business_form,
                                         'candidate_form': candidate_form,
                                         'interested_form': interested_form})

def thanks(request):
    return render(request, 'thanks.html')

def tests(request):
    return render(request, 'qunit-home.html')
