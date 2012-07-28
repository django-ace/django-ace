from __future__ import unicode_literals
from django import forms
from django.forms.util import flatatt
from django.utils.safestring import mark_safe


class AceWidget(forms.Textarea):
    def __init__(self, mode=None, theme=None, wordwrap=False, *args, **kwargs):
        self.mode = mode
        self.theme = theme
        self.wordwrap = wordwrap
        super(AceWidget, self).__init__(*args, **kwargs)

    @property
    def media(self):
        js = [
            "django_ace/ace/ace.js",
            "django_ace/widget.js",
        ]
        if self.mode:
            js.append("django_ace/ace/mode-%s.js" % self.mode)
        if self.theme:
            js.append("django_ace/ace/theme-%s.js" % self.theme)
        css = {
            "screen": ["django_ace/widget.css"],
        }
        return forms.Media(js=js, css=css)

    def render(self, name, value, attrs=None):
        attrs = attrs or {}

        ace_attrs = {
            "class": "django-ace-widget loading",
        }
        if self.mode:
            ace_attrs["data-mode"] = self.mode
        if self.theme:
            ace_attrs["data-theme"] = self.theme
        if self.wordwrap:
            ace_attrs["data-wordwrap"] = "true"

        textarea = super(AceWidget, self).render(name, value, attrs)
        return mark_safe('<div%s><div></div></div>%s' % (
                flatatt(ace_attrs), textarea))
