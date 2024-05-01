import re
from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'address', 'phone_number', 'email', 'birthday', 'note']

    def clean_phone_number(self):
        data = self.cleaned_data['phone_number']
        if not re.match(r'^\+?\d{1,5}?\d{9,15}$', data):
            raise forms.ValidationError("Invalid phone number")
        return data

    def clean_email(self):
        data = self.cleaned_data['email']
        if not re.match(r'^\S+@\S+\.\S+$', data):
            raise forms.ValidationError("Invalid email address")
        return data

    def save(self, commit=True):
        instance = super(ContactForm, self).save(commit=False)
        if commit:
            instance.save()
        return instance
