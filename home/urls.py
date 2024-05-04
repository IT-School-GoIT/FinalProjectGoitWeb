from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='home'),
    path('news', views.news, name='news'),
    path('project_topic', views.project_topic, name='project_topic'),
    path('exchange_rate', views.exchange_rate, name='exchange_rate'),

]
