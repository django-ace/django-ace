from django import forms
from django.contrib import admin
from django_ace import AceWidget

from .models import Snippet


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ("text",)
        widgets = {
            "text": AceWidget(
                mode="markdown", theme="twilight", width=None, height=None
            ),
        }


@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    form = SnippetForm
    readonly_fields = ("created_at",)
