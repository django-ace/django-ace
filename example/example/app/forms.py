from django import forms
from django_ace import AceWidget

from .models import Snippet


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        widgets = {
            "text": AceWidget(mode="html", theme="twilight", width=None, height=None),
        }
        exclude = ()
