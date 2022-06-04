from .views import EditUserView,Test
from django.urls import path
app_name='user_pro'

urlpatterns=[
    path('edite/',EditUserView.as_view(),name='edite'),
    path('test/',Test.as_view(),name='test'),
]
