from django.urls import path

from .views import CategoryListView, JobDetailView, JobListView

app_name = "job"
urlpatterns = [
    path("", CategoryListView.as_view(), name="category"),
    path("job/<int:id>/", JobDetailView.as_view(), name="detail"),
]
