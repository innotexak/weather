from django import forms 
from .models import WForm
# from django_countries.fields import CountryField

class WeatherForm(forms.ModelForm):
    # country = CountryField( max_length=100, blank_label='(select country)').formfield()
    # state = forms.CharField(max_length=50)
    # city = forms.CharField(max_length=50)
    class Meta:
        model = WForm
        fields = ['city']
        
        def __str__(self):
            return f"{self.city}"