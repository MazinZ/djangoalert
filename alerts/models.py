from django.db import models
from django.forms import ModelForm


# Create your models here.

class Alert(models.Model):
    alertName = models.CharField(max_length=50)
    alertText = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()