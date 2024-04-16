from django.urls import path
from . import views


app_name = 'comander'

urlpatterns = [
    path('', views.index, name='commands'),
    path('add', views.add, name='add'),
    path('search_all', views.search_all, name='search_all'),
    path('change', views.change, name='change'),
    path('delete', views.delete, name='delete'),
    path('sorting_files', views.sorting_files, name='sorting_files'),
    path('birhday_contact', views.birhday_contact, name='birhday_contact'),










]