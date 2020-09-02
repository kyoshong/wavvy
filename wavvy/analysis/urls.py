from django.urls import path
from . import views
from .views import WeatherDetailView


urlpatterns = [
    path('',views.grap,name='grap'),
    path('weather/',views.weather,name='weather'),
    path('weather/<int:pk>/',WeatherDetailView.as_view(),name='weather-detail'),
    path('weather/<int:pk>/',views.weather_list, name="weather"),
    
]
