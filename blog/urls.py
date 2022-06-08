from django.urls import path

from .views import ArticleDetailView, ArticleListView, CategoryListView

app_name = "blog"
urlpatterns = [
    path("", ArticleListView.as_view(), name="list"),
    path("category/", CategoryListView.as_view(), name="category"),
    path("article/<int:id>/", ArticleListView.as_view(), name="detail"),
]
