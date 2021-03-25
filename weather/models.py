from django.db import models

# Create your models here.

# from django import forms 
# from django_countries.fields import CountryField

class WForm(models.Model):
    city = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.city}"