import re
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import RegexValidator, EmailValidator
from django.core.exceptions import ValidationError


def validate_phone_number(value):
    if not re.match(r'^\+?\d{1,5}?\d{9,15}$', value):
        raise ValidationError('%(value)s is not a valid phone number.', params={'value': value},)


def clean_email(data):
    if not re.match(r'^\S+@\S+\.\S+$', data):
        raise ValidationError("Invalid email address")


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='contacts', default=1)
    name = models.CharField(max_length=255)
    address = models.CharField()
    phone_number = models.CharField(max_length=15, validators=[validate_phone_number])
    email = models.EmailField(validators=[EmailValidator])
    birthday = models.DateField()
    note = models.CharField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['name']
