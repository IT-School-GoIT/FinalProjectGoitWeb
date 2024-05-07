from django.contrib import admin

from .models import File, FileCategory, Profile


admin.site.register(File)
admin.site.register(FileCategory)
admin.site.register(Profile)
