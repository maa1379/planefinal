from django.urls import path

from .views import HotelRoomsView, HotelSearchView, HotelView,CitiesView

app_name = "hotel"
urlpatterns = [
    path("", HotelView.as_view(), name="list"),
    path("search/", HotelSearchView.as_view(), name="search"),
    path("rooms/<int:city_id>/", HotelRoomsView.as_view(), name="rooms"),
    path('cities/',CitiesView.as_view(),name='city_list'),
]
