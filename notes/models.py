from django.db import models
from django_project import settings
from django.contrib.auth import get_user_model

class Tag(models.Model):
    name = models.CharField(max_length=50, null=False)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=None)  # Используйте функцию get_user_model для получения модели пользователя

    class Meta:
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name
class Note(models.Model):
    name = models.CharField(max_length=50, null=False)
    description = models.TextField(null=False)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Notes"

    def __str__(self):
        return self.name