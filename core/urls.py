from django.urls import path

from .views import AboutUsView, ContactUsView, RulesView, WorkWithView

app_name = "core"
urlpatterns = [
    path("contact/", ContactUsView.as_view(), name="contact"),
    path("work/", WorkWithView.as_view(), name="work"),
    path("about_us/", AboutUsView.as_view(), name="about_us"),
    path("rules/", RulesView.as_view(), name="rules"),
]
