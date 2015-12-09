from django.shortcuts import render, redirect
from django.http import HttpResponse
from models import *

# Test view from Django tutorial: https://docs.djangoproject.com/en/1.9/intro/tutorial01/

def index(request):
    # Save email
    if request.method == 'POST':
        if 'business' in request.POST:
            business_name = request.POST['business_name']
            business_email = request.POST['business_email']
            Business.objects.create(name=business_name,
                                    email_address=business_email)
        elif 'candidate' in request.POST:
            candidate_email = request.POST['candidate_email']
            Candidate.objects.create(email_address=candidate_email)
        elif 'interested' in request.POST:
            interested_email = request.POST['interested_email']
            InterestedParty.objects.create(email_address=interested_email)

        out = redirect('/inployment/thanks/')
    else:
        out = render(request, 'home.html')
    return out

def thanks(request):
    return render(request, 'thanks.html')
