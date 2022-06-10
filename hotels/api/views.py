import json

import requests
from rest_framework import generics, status
from rest_framework.response import Response

from airlines.utils import Persian


class HotelApiView(generics.GenericAPIView):
    def get(self, request):
        response = requests.get('https://api.vhotel.ir/api/V4/hotels', auth=('admin', "iEol5iBJjFCRKIBA"))
        hotel_list = json.loads(response.content)
        return Response(hotel_list,status=status.HTTP_200_OK)


class CitiesView(generics.GenericAPIView):
    def get(self, request):
        get_data = requests.get(
            "https://api.vhotel.ir/api/V4/cities",
            auth=("admin", "iEol5iBJjFCRKIBA"),
        )
        hotel_list = json.loads(get_data.content)
        return Response(hotel_list,status=status.HTTP_200_OK)


class HotelsSearchApiView(generics.GenericAPIView):
    def get(self, request):
        go = Persian(request.GET.get("go")).gregorian_string()
        come = Persian(request.GET.get("come")).gregorian_string()
        city_id_code = request.GET.get('city_id')
        f = requests.Session()
        headers = {"content-type": "application/json"}
        my_data = {"availabilityByCityRq": {
            "cityId": city_id_code,
            "from": go,
            "to": come,
        }
        }
        get_data = f.post(
            "https://api.vhotel.ir/api/V4/availability",
            auth=("admin", "iEol5iBJjFCRKIBA"),
            data=json.dumps(my_data),
            timeout=30,
            headers=headers,
        )
        hotels_list = json.loads(get_data.content)
        return Response(hotels_list)