import requests
import json


class Service(object):
    @staticmethod
    def get_service_noaa(kwargs):
        method = 'GET'
        endpoint = 'noaa'
        payload = {'latlon': kwargs['latlon']}
        response = weather_service(method=method, endpoint=endpoint, payload=payload)
        response = float(response['today']['current']['fahrenheit'])
        return response

    @staticmethod
    def get_service_accuweather(kwargs):
        method = 'GET'
        endpoint = 'accuweather'
        payload = {'latitude': kwargs['lat'], 'longitude': kwargs['lon']}
        response = weather_service(method=method, endpoint=endpoint, payload=payload)
        response = float(response['simpleforecast']['forecastday'][0]['current']['fahrenheit'])
        return response

    @staticmethod
    def get_service_weather(kwargs):
        method = 'POST'
        endpoint = 'weatherdotcom'
        response = weather_service(method=method, endpoint=endpoint, data={'lat': kwargs['lat'], 'lon': kwargs['lon']})
        response = float(response['query']['results']['channel']['condition']['temp'])
        return response


def weather_service(method, endpoint, payload=None, data=None):
    url = "{}{}".format('http://localhost:5000/', endpoint)
    headers = {'content-type': 'application/json'}
    response = requests.request(method=method, url=url, params=payload,
                                data=json.dumps(data), headers=headers)
    return response.json()
