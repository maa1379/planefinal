import json
from copy import copy

import requests
from django.shortcuts import get_object_or_404, render
from django.views.generic import View

from .models import Airline
from .utils import Persian, city_name


class SearchListView(View):
    template_name = "airlines/search.html"

    def get(self, request):
        airlines_list = Airline.objects.all()
        trip_list_final = []
        fly_date = request.GET.get("date")
        month = fly_date[5:7]
        day = fly_date[8:]
        new_fly_date = Persian(fly_date).gregorian_string()
        for airline in airlines_list:
            trips = requests.get(
                f"{airline.base_url}/AvailabilityJS.jsp?AirLine={airline.symbol}&cbSource={request.GET.get('source')}&cbTarget={request.GET.get('target')}&cbDay1={day}&cbMonth1={month}&cbAdultQty={request.GET.get('adult', 0)}&cbChi%20dQty={request.GET.get('child', 0)}&cbInfantQty={request.GET.get('infant', 0)}&OfficeUser={airline.username}&OfficePass={airline.password}"
            )
            a = json.loads(trips.content)
            trip_list = a["AvailableFlights"]

            for i in trip_list:
                adultTotalPrices = str(i["AdultTotalPrices"]).split(" ")
                class_type = str(i["ClassesStatus"]).split(" ")
                number = len(adultTotalPrices)
                item_number = 0
                for name in range(number):
                    add = {
                        'class': class_type[name],
                        'price': adultTotalPrices[name].split(':')[1],
                        'fly_class':adultTotalPrices[name].split(':')[0],
                        'image': airline.logo.url,
                        'airline_id': airline.id,
                        'origin_city_name': city_name.get(i["Origin"]),
                        'airline_name': airline.name,
                        'DepartureTime': i["DepartureDateTime"][11:16],
                        'destination_city_name': city_name.get(i["Destination"]),
                        'ArrivalTime': i["ArrivalDateTime"][11:16],
                        'persian_date': i["DepartureDateTime"][:10],
                    }
                    if "C" in str(add["class"]):
                        add["class"] = "ظرفیت ندارد"
                    elif "A" in str(add['class']):
                        add['class'] = 'صندلی موجود بیشتر از 9 عدد'
                    elif "X" in str(add['class']):
                        add['class'] = 'کالس کنسل شده است و موجود نمی باشد.'
                    else:
                        add['clas'] = add['class'][-1]
                    number += 1
                    item_number += 1
                    if add['price'] != '-':
                        b = copy(i)
                        b.update(add)
                        trip_list_final.append(b)
                    else:
                        pass

        request.session["passenger_info"] = {
            "adult": request.GET.get("adult", 0),
            "child": request.GET.get("child", 0),
            "infant": request.GET.get("infant", 0),
        }
        flight_count = len(trip_list_final)
        return render(
            request,
            self.template_name,
            {
                "trip_list": trip_list_final,
                "flight_count": flight_count,
                "airline_list": airlines_list,
            },
        )
