from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.index, name='about'),
    path('contacts', views.index, name='contacts'),

]
