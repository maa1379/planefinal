from django.urls import path

from .views import EditUserView, Test

app_name = "user_pro"

urlpatterns = [
    path("edite/", EditUserView.as_view(), name="edite"),
    path("test/", Test.as_view(), name="test"),
]
