from django.urls import include, path

from hotels.api.urls import urlpatterns

from .views import CitiesView, HotelRoomsView, HotelSearchView, HotelView

app_name = "hotel"
urlpatterns = [
    path("", HotelView.as_view(), name="list"),
    path("search/", HotelSearchView.as_view(), name="search"),
    path("rooms/<int:city_id>/", HotelRoomsView.as_view(), name="rooms"),
    path('cities/',CitiesView.as_view(),name='city_list'),
    path('api/', include(urlpatterns)),
]
