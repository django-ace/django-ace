# -*- coding: utf-8 -*-
from django import forms

from django_ace import AceWidget
from .models import Snippet


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        widgets = {
            "text": AceWidget(
                mode='html', theme='twilight',
                wordwrap=True, showinvisibles=True, usesofttabs=False,
                tabsize=2, fontsize='12pt',
            ),
        }
        exclude = ()
