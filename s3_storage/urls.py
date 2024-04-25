from django.urls import path
from . import views

app_name = 's3_storage'

urlpatterns = [
    path('upload/', views.upload_file, name='upload'),
    path('list/', views.file_list, name='list'),
    path('download/<int:file_id>/', views.download_file, name='download'),
    path('delete/<int:file_id>/', views.delete_file, name='delete'),
]
