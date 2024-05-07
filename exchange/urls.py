from django.urls import path
from . import views

app_parsing = "exchange"

urlpatterns = [
    path("currency/", views.list_currency, name="currency"),
    path("add_currency/", views.add_currency, name="add_currency"),
]
