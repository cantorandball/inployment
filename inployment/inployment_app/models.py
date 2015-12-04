from __future__ import unicode_literals

from django.db import models

class Business(models.Model):
    name = models.TextField(default="")
    email_address = models.EmailField(default="")

class Candidate(models.Model):
    email_address = models.EmailField(default="")

class InterestedParty(models.Model):
    email_address = models.EmailField(default="")


