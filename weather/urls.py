from django.urls import path
from django.conf.urls.static import static 
from django.conf import settings 
from . import views

urlpatterns = [
    path('forecast/', views.weather_view, name='forecast'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)