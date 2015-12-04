from django.shortcuts import render
from django.http import HttpResponse
from inployment.inployment_app.models import *

# Test view from Django tutorial: https://docs.djangoproject.com/en/1.9/intro/tutorial01/

def index(request):
    # Save email
    if request.method == 'POST':
        if request.POST['business_email']:
            business_email = request.POST['business_email']
            Business.objects.create(email_address=business_email)
        if request.POST['candidate_email']:
            candidate_email = request.POST['candidate_email']
            Candidate.objects.create(email_address=candidate_email)
        if request.POST['interested_email']:
            interested_email = request.POST['interested_email']
            InterestedParty.objects.create(email_address=interested_email)

    return render(request, 'home.html')
