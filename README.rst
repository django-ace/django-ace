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

To deactivate the syntax checker completely, disable the Web Worker::

    class EditorForm(forms.Form):
        text = forms.CharField(widget=AceWidget(
            mode='css', theme='twilight', use_worker=False
        ))


All options are::

    class EditorForm(forms.Form):
        text = forms.CharField(widget=AceWidget(
            mode="python",
            theme="dawn",
            use_worker=True,
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

    # install in virtualenv
    cd example/
    virtualenv .env
    . .env/bin/activate
    pip install -e ..
    # prepare sqlite database
    ./manage.py makemigrations app
    ./manage.py migrate
    # user for admin access
    ./manage.py createsuperuser
    # run dev-server
    ./manage.py runserver

Then browser to ``http://localhost:8000`` or ``http://localhost:8000/admin``.


Change log
==========

v1.1.0
------

- Update ACE editor to version v1.4.11
- Rewrite of init() function to support admin inline-forms
- New widget option ``use_worker``
- Use template engine to generate widget HTML
- Rewrite of boolean data attributes
- Add tests, update example with admin integration


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
