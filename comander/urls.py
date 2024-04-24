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
    path('download', views.download, name='download'),
    path('view_file', views.view_file, name='view_file'),
    path('contact_card', views.contact_card, name='contact_card'),
    path('deleted_done', views.deleted_done, name='deleted_done'),
    path('change_done', views.change_done, name='change_done'),
    path('add_note', views.add_note, name='add_note'),
    path('all_notes', views.all_notes, name='all_notes'),
    path('change_note', views.change_note, name='change_note'),
    path('change_note_done', views.change_note_done, name='change_note_done'),
    










]