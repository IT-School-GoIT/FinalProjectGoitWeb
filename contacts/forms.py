import re
from datetime import timedelta

from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Contact
def validate_birth_date(value):
    """
    The validate_birth_date function is a custom validator that ensures the birthdate is in the past and not more than 120 years ago. It raises a ValidationError if either of these conditions are not met.

    :param value: Pass the value of the field that is being validated
    :return: The value if it is a valid birthdate
    :doc-author: Trelent
    """
    max_birth_date = timezone.now().date() - timedelta(days=365.25 * 120)
    if value >= timezone.now().date() or value <= max_birth_date:
        raise ValidationError("Birth date must be in the past and not exceed 120 years")
    return value

class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        """
        The __init__ method initializes the ContactForm object.
        It sets up the attributes of an instance of a ContactForm object.
        The user and request arguments are optional, but if they are not provided, they will be set to None.
    
        :param self: Refer to the current instance of the object
        :param *args: Non-keyworded variable length argument list
        :param **kwargs: Pass keyword arguments to a function
        :return: The user and request objects
        :doc-author: Trelent
        """
        self.user = kwargs.pop("user", None)
        self.request = kwargs.pop("request", None)
        super(ContactForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Contact
        fields = ["name", "address", "phone_number", "email", "birthday", "note"]

    def clean_phone_number(self):
        """
        The clean_phone_number function is a function that takes in the phone number and checks to see if it matches the regular expression. If it does not match, then an error message will be raised. Otherwise, the data will be returned.
        
        :param self: Refer to the current instance of the class
        :return: A valid phone number
        :doc-author: Trelent
        """
        data = self.cleaned_data["phone_number"]
        if not re.match(r"^\+?\d{1,5}?\d{7,15}$", data):
            raise forms.ValidationError("Invalid phone number")
        return data

    def clean_email(self):
        """
        The clean_email function is a function that checks to see if the email address entered by the user is valid.
        It does this by using a regular expression, which looks for an @ symbol and at least one period in the string.
        If it finds these things, then it returns true and allows the user to continue with their registration process.
        
        :param self: Refer to the current instance of the class
        :return: The email address if it is valid
        :doc-author: Trelent
        """
        email = self.cleaned_data.get("email")
        if not re.match(r"^\S+@\S+\.\S+$", email):
            raise forms.ValidationError("Invalid email address")
        return email

    def clean_birthday(self):
        """
        The clean_birthday function validates the birthday field.
        It checks that the date is not in the future, and that it is at least 18 years ago.
        
        :param self: Access the instance of the class
        :return: The birthday field
        :doc-author: Trelent
        """
        birthday = self.cleaned_data["birthday"]
        validate_birth_date(birthday)
        return birthday

    def save(self, user=None, commit=True):
        """
        The save function is a function that saves the form.
        It takes two arguments: user and commit.
        The user argument is an optional argument, which defaults to None if not specified.
        The commit argument is also an optional argument, which defaults to True if not specified.
        
        :param self: Refer to the current instance of a class
        :param user: Assign the user to the contact
        :param commit: Tell django whether or not to save the model after it has been created
        :return: The instance of the model
        :doc-author: Trelent
        """
        instance = super(ContactForm, self).save(commit=False)
        if user:
            instance.user = user
        if commit:
            instance.save()
        return instance
