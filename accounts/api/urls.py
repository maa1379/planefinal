from django.urls import path

from .views import (LoginApiView, Logout, PasswordChangeApiView,
                    RegisterUserApiView, RegisterVerifyApiView,
                    UserUpdateApiView)

app_name='api'
urlpatterns = [
    path("login/", LoginApiView.as_view(), name="api_login"),
    path("password_change/",PasswordChangeApiView.as_view(),name='api_password_change'),
    path('logout/',Logout.as_view(),name='api_logout'),
    path('register/',RegisterUserApiView.as_view(),name='api_register'),
    path('verify/',RegisterVerifyApiView.as_view(),name='api_verify'),
    path('update/',UserUpdateApiView.as_view(),name='api_update'),
    # path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
