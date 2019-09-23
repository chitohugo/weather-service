from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import Service

servi = Service()


class WeatherServiceList(APIView):
    @staticmethod
    def get(request):
        """
        Return current average temperature.

        :param latitude: float. (33.4)
        :param logintude: float. (44.0)
        :param list_services: string of service. ('noaa', 'accuweather', 'weather')
        """

        # Validate fields 
        if not request.query_params.get('latitude', '') and not request.query_params.get('longitude', ''):
            return Response("Required fields", status=status.HTTP_400_BAD_REQUEST)

        if not request.query_params.get('latitude', ' '):
            return Response("Required is latitude", status=status.HTTP_400_BAD_REQUEST)

        if not request.query_params.get('longitude', ' '):
            return Response("Required is longitude", status=status.HTTP_400_BAD_REQUEST)

        # Validate services 
        if not request.query_params.get('list_services', ''):
            return Response("Required is list_services", status=status.HTTP_400_BAD_REQUEST)

        params_services = ['noaa', 'accuweather', 'weather']
        list_services = request.query_params.get('list_services').split(',')
        services = [item for item in list_services if item in params_services]

        if not services:
            return Response("You must add one of these services: ['noaa', 'accuweather', 'weather']",
                            status=status.HTTP_400_BAD_REQUEST)

        lat, lon = float(request.query_params.get('latitude')), float(request.query_params.get('longitude'))
        kwargs = {
            "lat": lat,
            "lon": lon,
            "latlon": "{},{}".format(lat, lon)
        }
        filters_services = {
            "noaa": servi.get_service_noaa,
            "accuweather": servi.get_service_accuweather,
            "weather": servi.get_service_weather,
        }

        results = [filters_services[service](kwargs) for service in services]
        average = sum(results)
        average = average / len(results)
        celsius = (average - 32) * 5 / 9
        data = {"data": "Current average temperature is: {}.F or {}.C".format(int(average), int(celsius))}
        return Response(data=data, status=status.HTTP_200_OK)
