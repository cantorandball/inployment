from __future__ import unicode_literals

from django.db import models

# Create your models here.
class PotentialUser(models.Model):
    email_address = models.TextField(default="")

