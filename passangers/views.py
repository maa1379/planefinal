import datetime
import json
import logging

import requests
# from azbankgateways import bankfactories
# from azbankgateways import default_settings as settings
# from azbankgateways import models as bank_models
# from azbankgateways.exceptions import AZBankGatewaysException
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
#
#
# # Create your views here.
#
#
# class ReserveCreateView(View):
#     form_class = PassengerForm
#     template_name = "passengers/reserve.html"
#
#     def get(self, request):
#         return render(request, self.template_name, {"form": self.form_class})
#
#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             cd = form.save(commit=False)
#             cd.reserver = request.user
#             cd.fly_code = request.POST.get("fly_code")
#             cd.save()
#             messages.success(request, "", "success")
#             return redirect()
#         else:
#             messages.error(request, "", "danger")
#         return render(request, self.template_name, {"form": form})
from django.views import View

from airlines.models import Airline
from passangers.models import Passenger

from .models import Passenger, Reservation

# from django.views.generic import View
#





def home(request):
    return render(request, "index.html")


class PassengerView(View):
    template_name = "passengers/passengers.html"

    def get(self, request):
        info = {
            "airline_name": request.GET.get("airline_name"),
            "DepartureTime": request.GET.get("DepartureTime"),
            "ArrivalTime": request.GET.get("ArrivalTime"),
            "Destination": request.GET.get("Destination"),
            "date": request.GET.get("persian_date"),
            "origin": request.GET.get("origin_city_name"),
            "destination": request.GET.get("destination_city_name"),
            "logo": request.GET.get("trip_image"),
            'fly_code': request.GET.get('fly_code_number',None),
            'fly_class': request.GET.get('fly_class_code')
        }
        context = {}

        try:
            # context['passenger_info'] = request.session['passenger_info']
            passenger_number = request.session["passenger_info"]
            context["passenger_info"] = passenger_number

        except:
            context["passenger_info"] = {}
        airline = Airline.objects.get(name=info.get("airline_name"))
        # price = requests.get(
        #     f'{airline.base_url}/FareJS.jsp?AirLine={airline.symbol}&Route={request.GET.get("Origin")}-{request.GET.get("Destination")}&RBD={request.GET.get("fly_code")}&DepartureDate={request.GET.get("persian_date")}&FlightNo={request.GET.get("flight_no")}&OfficeUser={airline.username}&OfficePass={airline.password}')
        # price_list = json.loads(price.content.decode('ISO-8859-1'))
        # prices = {'adult': price_list["AdultTotalPrice"], 'child': price_list["ChildTotalPrice"],
        #           'infant': price_list["InfantTotalPrice"]}
        context['price_list']: prices
        context["air_line"] = airline
        context["info"] = info
        return render(request, self.template_name, context)

    def post(self, request):
        # email = request.user.profile.email
        phone_number = request.user.phone_number
        airline = Airline.objects.first()
        if request.POST.get("email"):
            email = request.POST.get("email")
            phone_number = request.POST.get("phone_number")

        reserve = Reservation.objects.create(
            user_id=request.user.id,
            air_line=airline,
            fly_code=request.POST.get("fly_code"),
            flight_class=request.POST.get('fly_class'),
            source=request.POST.get("source"),
            target=request.POST.get("target"),
            date=request.POST.get("date"),
            email="elel@fmal.com",
            phone_number=phone_number,
            paid=False,
        )
        passengers = []
        for key, value in dict(request.POST).items():
            for i in range(0, len(value)):
                if len(passengers) > i:
                    passenger = passengers[i]
                else:
                    passenger = Passenger()
                    passenger.price = 0
                    passenger.reserve = reserve
                if key == "latinName":
                    passenger.en_name = value[i]
                elif key == "date":
                    passenger.date = value[i]
                elif key == "latinFamilyName":
                    passenger.en_family = value[i]
                elif key == "gender":
                    passenger.gender = value[i]
                elif key == "nationalCode":
                    passenger.national_code = value[i]
                elif key == "name":
                    passenger.ir_name = value[i]
                elif key == "familyName":
                    passenger.ir_family = value[i]
                if len(passengers) > i:
                    passengers[i] = passenger
                else:
                    passengers.append(passenger)

        Passenger.objects.bulk_create(passengers)
        return redirect("passengers:trip")


class TripInfoView(View):
    def get(self, request):
        reserve_obj = Reservation.objects.last()
        return render(request, "passengers/infoSubmit.html", {"reserve": reserve_obj})


class CancelTicketView(View):
    def get(self, request, reserve_id):
        reserve_obj = get_object_or_404(Reservation, id=reserve_id)
        reserve_obj.delete()
        return redirect("passengers:home")


class Reserve(View):
    def get(self, request):
        reserve_obj = Reservation.objects.first()
        # for i in reserve_obj.
        requests.get(
            f"{reserve_obj.air_line.base_url}/ReservJS?AirLine={reserve_obj.air_line.symbol}&cbSource={reserve_obj.source}&cbTarget={reserve_obj.target}Q&FlightClass={reserve_obj.flight_class}&FlightNo={reserve_obj.flight_no}&Day&Month&No=1&edtName1={reserve_obj.first_name}&edtLast1={reserve_obj.last_name}&edtAge1={reserve_obj.age}&edtID1={reserve_obj.national_code}&edtContact={reserve_obj.phone_number}&DepartureDate=2022-03-03&OfficeUser={reserve_obj.air_line.username}&OfficePass{reserve_obj.air_line.password}"
        )


def go_to_gateway_view(request):
    pass
    amount = 1000
    user_mobile_number = "+989112221234"
    info = {
        "ResNum": "111111",
        "amount": amount,
        "cell": user_mobile_number,
    }
    return render(request, "passengers/payTest.html", {"info": info})
    # factory = bankfactories.BankFactory()
    # try:
    #     bank = factory.auto_create()
    #     bank.set_request(request)
    #     bank.set_amount(amount)
    #     bank.set_client_callback_url(reverse("callback-gateway"))
    #     bank.set_mobile_number(user_mobile_number)  # اختیاری
    #
    #     bank_record = bank.ready()
    #
    #     return bank.redirect_gateway()
    # except AZBankGatewaysException as e:
    #     logging.critical(e)
    #     # TODO: redirect to failed page.
    #     raise e


def cities(request):
    # re = requests.get('https://api.vhotel.ir/api/V4/cities', auth=('admin', "iEol5iBJjFCRKIBA"))
    # data = re.text
    data = {
        "ABD": "آبادان",
        "AKW": "آقاجاری",
        "AEU": "ابوموسی",
        "AJK": "اراک",
        "ADU": "اردبیل",
        "OMH": "ارومیه",
        "IFN": "اصفهان",
        "OMI": "امیدیه",
        "AWZ": "اهواز",
        "IHR": "ایران شهر",
        "IIL": "ایلام",
        "BBL": "بابلسر",
        "BJB": "بجنورد",
        "BXR": "بم",
        "BND": "بندر عباس",
        "BDH": "بندر لنگه",
        "MRX": "بندر ماهشهر",
        "IAQ": "بهرگان",
        "BUZ": "بوشهر",
        "XBJ": "بیرجند",
        "BSM": "بیشه کلا",
        "PFQ": "پارس آباد",
        "TBZ": "تبریز",
        "TCX": "طبس",
        "IKA": "تهران(امام خمینی)",
        "THR": "تهران",
        "TEW": "توحید",
        "KHK": "جزیره خارک",
        "SXI": "جزیره سیری",
        "KIH": "جزیره کیش",
        "JYR": "جیرفت",
        "ZBR": "چابهار",
        "KHA": "خانه",
        "KHD": "خرم آباد",
        "KHY": "خوی",
        "DEF": "دزفول",
        "RZR": "رامسر",
        "RAS": "رشت",
        "RJN": "رفسنجان",
        "ACZ": "زابل",
        "ZAH": "زاهدان",
        "JWN": "زنجان",
        "SRY": "ساری",
        "AFZ": "سبزوار",
        "CKT": "سرخس",
        "SDG": "سنندج",
        "ACP": "سهند",
        "SYJ": "سیرجان",
        "CQD": "شهر کرد",
        "SYZ": "شیراز",
        "PGU": "عسلویه",
        "FAZ": "فاسا",
        "GZW": "قزوین",
        "GSM": "قشم",
        "GCH": "گچساران",
        "GBT": "گورگن",
        "LRR": "لار",
        "LFM": "لامرد",
        "LVP": "لاوان",
        "MHD": "مشهد",
        "NUJ": "نوژه",
        "NSH": "نوشهر",
        "IFH": "هسا",
        "HDM": "همدان",
        "HDR": "هوادریا",
        "KNR": "کانگان",
        "KER": "کرمان",
        "KSH": "کرمانشاه",
        "KLM": "کلاله",
        "YES": "یاسوج",
        "AZD": "یزد",
    }

    # serialize data obj as a JSON stream
    data = json.dumps(data)
    response = HttpResponse(data, content_type="application/json charset=utf-8")

    return response
