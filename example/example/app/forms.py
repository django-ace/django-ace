from .models import Snippet
from django import forms
from django_ace import AceWidget


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        widgets = {
            "text": AceWidget(theme='twilight'),
        }

    def clean_text(self):
        value = self.cleaned_data["text"]
        if not "valid" in value:
            raise forms.ValidationError("Must contain the string 'valid'")
        return value
