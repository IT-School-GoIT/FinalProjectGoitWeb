from django.urls import path
from . import views


app_name = "comander"

urlpatterns = [
    path("", views.index, name="commands"),
    path("add", views.add, name="add"),
    path("search_all", views.search_all, name="search_all"),
    path("change", views.change, name="change"),
    path("delete", views.delete, name="delete"),
    path("deleted_done", views.deleted_done, name="deleted_done"),
    path("sorting_files", views.sorting_files, name="sorting_files"),
    path("birhday_contact", views.birhday_contact, name="birhday_contact"),
    path("download", views.download, name="download"),
    path("view_file", views.view_file, name="view_file"),
    path("contact_card", views.contact_card, name="contact_card"),
    path("change_done", views.change_done, name="change_done"),
    path("add_note", views.add_note, name="add_note"),
    path("all_notes", views.all_notes, name="all_notes"),
    path("change_note", views.change_note, name="change_note"),
    path("change_note_done", views.change_note_done, name="change_note_done"),
    path("deleted_note", views.deleted_note, name="deleted_note"),
    path("files", views.files, name="files"),
    path("file_upload_done", views.file_upload_done, name="file_upload_done"),
    path("change_file", views.change_file, name="change_file"),
    path("change_file_done", views.change_file_done, name="change_file_done"),
    path("deleted_file_done", views.deleted_file_done, name="deleted_file_done"),
]
