from django.urls import path
from . import views

app_parsing = "parsing"

urlpatterns = [
    path("news/", views.list_news, name="news"),
    path("add_news/", views.add_news, name="add_news"),
]
