from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('forecast/', views.weather_view, name='forecast'),
] 