from django.urls import path
from _codeiro.weather_services import views

urlpatterns = [
    path('weather_services/', views.WeatherServiceList.as_view())

]