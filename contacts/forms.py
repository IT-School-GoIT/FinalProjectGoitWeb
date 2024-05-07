import re
from datetime import timedelta

from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Contact


def validate_birth_date(value):
    """
    Validate that the birth date is in the past and does not exceed 120 years.
    """
    max_birth_date = timezone.now().date() - timedelta(days=365.25 * 120)
    if value >= timezone.now().date() or value <= max_birth_date:
        raise ValidationError("Birth date must be in the past and not exceed 120 years")
    return value


class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        self.request = kwargs.pop("request", None)
        super(ContactForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Contact
        fields = ["name", "address", "phone_number", "email", "birthday", "note"]

    def clean_phone_number(self):
        data = self.cleaned_data["phone_number"]
        if not re.match(r"^\+?\d{1,5}?\d{7,15}$", data):
            raise forms.ValidationError("Invalid phone number")
        return data

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not re.match(r"^\S+@\S+\.\S+$", email):
            raise forms.ValidationError("Invalid email address")
        return email

    def clean_birthday(self):
        birthday = self.cleaned_data["birthday"]
        validate_birth_date(birthday)
        return birthday

    def save(self, user=None, commit=True):
        instance = super(ContactForm, self).save(commit=False)
        if user:
            instance.user = user
        if commit:
            instance.save()
        return instance
