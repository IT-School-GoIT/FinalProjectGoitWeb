from django.urls import path, include
from django.views.generic import RedirectView

from . import views

app_name = 'contacts'


urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url='/static/images/favicon.ico')),
    path('contact_list/', views.contact_list, name='contact_list'),
    path('create/', views.create_contact, name='create'),
    path('edit_contact/<int:contact_id>/', views.edit_contact, name='edit_contact'),
    path('delete_contact/<int:contact_id>/', views.delete_contact, name='delete_contact'),
    path('contacts_with_birthday/', views.get_contacts_with_birthday_in, name='contacts_with_birthday'),


]