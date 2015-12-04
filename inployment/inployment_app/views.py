from django.shortcuts import render
from django.http import HttpResponse
from inployment.inployment_app.models import PotentialUser

# Test view from Django tutorial: https://docs.djangoproject.com/en/1.9/intro/tutorial01/

def index(request):
    # Save email
    if request.method == 'POST':
        curious_email = request.POST['curious_email']
        PotentialUser.objects.create(email_address=curious_email)

    return render(request, 'home.html')
