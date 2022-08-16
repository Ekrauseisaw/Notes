from django import forms
from .models import Note, Content


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['text']
        labels = {'text': ''}


class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}