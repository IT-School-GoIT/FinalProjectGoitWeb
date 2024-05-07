from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='contacts')
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    birthday = models.DateField()
    time_create = models.DateTimeField(default=timezone.now)
    note = models.CharField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
