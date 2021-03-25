from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import WeatherForm
import requests
import json
import datetime
from django.conf import settings 
from requests.exceptions import HTTPError


api_key = settings.API_KEY



def weather_view(request):
    city = request.GET.get('city')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    details = []
    try:
        response = requests.get(url)
    except:
        print("Error occured!")
        
        
    json_response = response.json() 
    time = datetime.datetime.now()     
    server_response = {
        'description':json_response['weather'][0]['description'],
        'cloud':json_response['clouds']['all'],
        'wind':json_response['wind']['speed'],
        'min_temp':int(json_response['main']['temp_min'] - 273.15 ),
        'max_temp':int(json_response['main']['temp_max'] - 273.15 ),
        'state':json_response['name'],
        'country':json_response['sys']['country'],
        'timestamp': f'{time.strftime("%c")}'
        }
    details.append(server_response)        
    form = WeatherForm()
    return render(request, 'index.html', {
                                            'detailed_data': details,
                                            'forms':form
                                            })
