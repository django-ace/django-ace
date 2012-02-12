from django import forms
from django.template import loader
from django.utils.encoding import force_unicode
from django.utils import formats

class CodeEditorWidget(forms.Widget):
    @property
    def media(self):
        scripts = ["ace_editor/ace/ace.js", "ace_editor/ace_editor.js"]
        if self.mode:
            scripts.append("ace_editor/ace/mode-{0}.js".format(self.mode))

        stylesheets = {'all': ('ace_editor/ace_editor.css',)}
        return forms.Media(js=scripts, css=stylesheets)

    template_name = 'ace_editor/ace_editor.html'

    def __init__(self, mode = None, *args, **kwargs):
        self.mode = mode
        super(CodeEditorWidget, self).__init__(*args, **kwargs)

    def _format_value(self, value):
        if self.is_localized:
            value = formats.localize_input(value)
        return force_unicode(value)

    def get_context(self, name, value, attrs=None):
        context = {
            'name': name,
            'mode': self.mode,
            'required': self.is_required,
            'True': True,
            }
        # True is injected in the context to allow stricter comparisons
        # for widget attrs. See:
        # https://github.com/brutasse/django-floppyforms/issues/25
        if self.is_hidden:
            context['hidden'] = True

        if value is None:
            value = ''

        if not '\n' in value:
            # The code editor messes up if there's only a single line.
            value += '\n'

        context['value'] = self._format_value(value)
        context['attrs'] = self.build_attrs(attrs)

        for key in context['attrs']:
            attr = context['attrs'][key]
            if attr == 1:
                # 1 == True so 'key="1"' will show up only as 'key'
                # Casting to a string so that it doesn't equal to True
                # See:
                # https://github.com/brutasse/django-floppyforms/issues/25
                if not isinstance(attr, bool):
                    context['attrs'][key] = str(attr)

        return context

    def render(self, name, value, attrs=None, **kwargs):
        context = self.get_context(name, value, attrs=attrs or {}, **kwargs)
        if not isinstance(value, basestring):
            value = ''
        if not '\n' in value:
            value += '\n'
        print "RENDERING"
        return loader.render_to_string(self.template_name, context)