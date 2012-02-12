# Django Ace Editor

This is an implementation of the [Ace-Editor](https://github.com/ajaxorg/ace/)
by ajax.org for Django. It's only supported by Python 1.3 as we make use of
staticfiles bundled with the application.

## Basic usage

    import ace_editor

    class MyAdminForm(forms.ModelForm):
        some_code = forms.CharField(widget=ace_editor.CodeEditorWidget())


You can also specify which language you are editing in which will set the
appropriate syntax highlighting and static analysis:

    class MyAdminForm(forms.ModelForm):
        custom_css = forms.CharField(widget=ace_editor.CodeEditorWidget(mode='css'))

## Installation

    You'll need to have `django.contrib.staticfiles` in `INSTALLED_APPS` and
    have set `STATIC_URL` so the apps js/css files can load.

    pip install -e git+git://github.com/Celc/markdown-urlize.git#egg=markdown-urlize

    Add `ace_editor` to your `INSTALLED_APPS`.