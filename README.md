# weather-service

### Setup
```
virtualenv env or python -m venv env
pip install -r requirements.txt
python manage.py runserver
```

### Route
Host: http://127.0.0.1:8000/
##### API WEATHER SERVICE
GET /api/weather_services/?latitude=33&longitude=44&list_services=noaa,weather,accuweather

___________________________________________________________

# mock-weather-api
Mock API for getting weather data

### Setup
```
https://github.com/otterlogic/mock-weather-api
virtualenv env
source env/bin/activate
pip install -r requirements.txt
FLASK_APP=app.py flask run
```
