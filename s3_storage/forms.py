from django import forms
from .models import File, Profile


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ["original_filename", "category", "description"]


class ProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput())

    class Meta:
        model = Profile
        fields = ["avatar"]
