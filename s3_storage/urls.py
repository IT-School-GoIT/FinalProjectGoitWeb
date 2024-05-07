from django.urls import path
from . import views

app_name = "s3_storage"

urlpatterns = [
    path("upload/", views.upload_file, name="upload"),
    path("list/", views.file_list, name="list"),
    path("download/<int:file_id>/", views.download_file, name="download"),
    path("edit_file/<int:file_id>/", views.edit_file, name="edit_file"),
    path("delete/<int:file_id>/", views.delete_file, name="delete"),
    path("create_category/", views.create_category, name="create_category"),
    path("edit_category/<int:category_id>/", views.edit_category, name="edit_category"),
    path(
        "delete_category/<int:category_id>/",
        views.delete_category,
        name="delete_category",
    ),
    path("categories/", views.category_list, name="category_list"),
    path("profile/", views.profile, name="profile"),
    path("profile_settings/", views.profile_settings, name="profile_settings"),
]
