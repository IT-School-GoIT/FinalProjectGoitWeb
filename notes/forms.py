from django import forms
from django.forms import ModelForm
from .models import Tag, Note

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name']


class NoteForm(ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)

    class Meta:
        model = Note
        fields = ['name', 'description', 'tags']


class NoteDoneForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['done']


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)

    def clean_query(self):
        query = self.cleaned_data.get('query')
        if query and len(query) < 3:
            raise forms.ValidationError("Query should be at least 3 characters long.")
        return query