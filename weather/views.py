from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import WeatherForm
import requests
import json
from django.conf import settings 
from requests.exceptions import HTTPError


api_key = settings.API_KEY

def home_view(request):
    
    return render(request, 'index.html', {})


def weather_view(request):
    # buffer = io.BytesIO()
    city = request.GET.get('city')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    details = []
    response = requests.get(url)
    json_response = response.json()      
    response = {
        'description':json_response['weather'][0]['description'],
        'cloud':json_response['clouds']['all'],
        'wind':json_response['wind']['speed'],
        'min_temp':int(json_response['main']['temp_min'] - 273.15 ),
        'max_temp':int(json_response['main']['temp_max'] - 273.15 ),
        'state':json_response['name'],
        'country':json_response['sys']['country'],
        }
    details.append(response)
        
    form = WeatherForm()

    return render(request, 'forecast.html', {
                                            'detailed_data': details,
                                            'forms':form
                                            })
