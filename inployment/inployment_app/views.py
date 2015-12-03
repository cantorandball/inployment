from django.shortcuts import render
from django.http import HttpResponse

# Test view from Django tutorial: https://docs.djangoproject.com/en/1.9/intro/tutorial01/

def index(request):
    return HttpResponse("This is a little tiny acorn of a website. Make it grow.")
