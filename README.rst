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

All options, and their default values, are::

    class EditorForm(forms.Form):
        text = forms.CharField(widget=AceWidget(
            mode=None,  # try for example "python"
            theme=None,  # try for example "twilight"
            wordwrap=False,
            width="500px",
            height="300px",
            minlines=None,
            maxlines=None,
            showprintmargin=True,
            showinvisibles=False,
            usesofttabs=True,
            tabsize=None,
            fontsize=None,
            toolbar=True,
            readonly=False,
            showgutter=True,  # To hide/show line numbers
            behaviours=True,  # To disable auto-append of quote when quotes are entered
        ))


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

v1.15.4
-------

- Added CSS to work with new admin in Django 4.2. Now you can use `width="100%"` without breaking the layout.

v1.15.3
-------

- Update ACE editor to version v1.15.3.

v1.14.0
-------

- Update ACE editor to version v1.14.0.
- Follow ACE version numbers.

v1.0.13
-------

- Update ACE editor to version v1.11.2.


v1.0.12
-------

- Update ACE editor to version v1.5.0.

v1.0.11
-------

- Support Grappelli inlines.


v1.0.10
-------

- FIX JavaScript error when using ``JavaScriptCatalog``.


v1.0.9
------

- New widget option ``showgutters`` to hide line numbers.
- New widget option ``behaviours`` to avoid auto-insert of quotes.


v1.0.8
------

- New widget option ``readonly``.
- Update ACE editor to version v1.4.12.


v1.0.7
------

- New widget option ``toolbar``.
- Update ACE editor to version v1.4.8.


v1.0.6
------

- New widget option ``fontsize``.
- Update ACE editor to version v1.4.7.


v1.0.5
------

- New widget option ``tabsize``.
- Upgrade ACE editor to version v1.4.2.


v1.0.4
------

- Update Django compatibility to ``>1.11,<=2.1``
- New widget options ``minLines``, ``maxLines``, ``showinvisibles``, ``usesofttabs``.
- Upgrade ACE editor to version v1.4.0.
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
