==========
django-ace
==========


Usage
=====

::

    from django import forms
    from django_ace import AceWidget

    class EditorForm(forms.Form):
        text = forms.CharField(widget=AceWidget)

Syntax highlighting and static analysis can be enabled by specifying the
language::

    class EditorForm(forms.Form):
        text = forms.CharField(widget=AceWidget(mode='css'))

Themes are also supported::

    class EditorForm(forms.Form):
        text = forms.CharField(widget=AceWidget(mode='css', theme='twilight'))

Additional options are::

    class EditorForm(forms.Form):
        text = forms.CharField(widget=AceWidget(wordwrap=False, width="500px", height="300px", showprintmargin=True))


Install
=======

1. Install using pip::

    pip install django_ace

2. Update ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        # ...
        'django_ace',
    )


Example Project
===============

There's an example project included in the source, to try it do::

    cd example/
    virtualenv .env
    . .env/bin/activate
    pip install -e ..
    ./manage.py makemigrations app
    ./manage.py migrate
    ./manage.py runserver

Then browser to ``http://localhost:8000``.


Change log
==========

v1.0.3
------

- Upgrade ACE editor to version 1.2.6
- Updated example for Django 1.11
- PEP8 improvements

v1.0.2
------

- Upgrade ACE editor to version 1.1.8
- Add support for showprintmargin

v1.0.1
------

- Add support for Django 1.7 by removing deprecated imports.

v1.0.0
------

- Initial release.
