from .models import Snippet
from django import forms
from django_ace import AceWidget


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        widgets = {
            "text": AceWidget(mode='html', theme='twilight'),
        }
        exclude = ()
