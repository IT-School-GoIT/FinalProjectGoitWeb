from django.contrib import admin

from .models import File, FileCategory


admin.site.register(File)
admin.site.register(FileCategory)
