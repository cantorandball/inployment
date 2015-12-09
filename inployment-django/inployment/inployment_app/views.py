from django.shortcuts import render, redirect
from django.http import HttpResponse
from models import *
from forms import *

# Test view from Django tutorial: https://docs.djangoproject.com/en/1.9/intro/tutorial01/

def index(request):
    # Save email
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
            candidate_email = request.POST['candidate_email']
            Candidate.objects.create(email_address=candidate_email)
        elif 'interested' in request.POST:
            interested_email = request.POST['interested_email']
            InterestedParty.objects.create(email_address=interested_email)

    else:
        business_form = BusinessForm()

    return render(request, 'home.html', {'business_form':business_form})


def thanks(request):
    return render(request, 'thanks.html')
