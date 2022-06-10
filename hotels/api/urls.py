from django.urls import path

from .views import CitiesView, HotelApiView, HotelsSearchApiView

urlpatterns = [
    path('cities/',CitiesView.as_view(),name='cities_api'),
    path('search/',HotelsSearchApiView.as_view(),name='search_api'),
    path('list/',HotelApiView.as_view(),name='list_api'),
]
