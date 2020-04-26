# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest

import django
import html5lib
from django.conf import settings
from django.utils import safestring

import django_ace


class TestWidget(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        settings.configure(TEMPLATES=[{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
        }])
        django.setup()

    def test_media(self):
        expected_js = ['django_ace/ace/ace.js', 'django_ace/widget.js']
        expected_css = {'screen': ['django_ace/widget.css']}

        ace_widget = django_ace.AceWidget()
        self.assertEqual(ace_widget.media._css, expected_css)
        self.assertEqual(ace_widget.media._js, expected_js)

        ace_widget = django_ace.AceWidget(mode='python')
        self.assertEqual(ace_widget.media._css, expected_css)
        self.assertEqual(
            ace_widget.media._js,
            expected_js + ['django_ace/ace/mode-python.js'],
        )

        ace_widget = django_ace.AceWidget(theme='monokai')
        self.assertEqual(ace_widget.media._css, expected_css)
        self.assertEqual(
            ace_widget.media._js,
            expected_js + ['django_ace/ace/theme-monokai.js'],
        )

    def test_render(self):
        ace_widget = django_ace.AceWidget()
        content = ace_widget.render('name', 'value')

        self.assertIsInstance(content, safestring.SafeText)
        expected_content = '' \
            '<div class="django-ace-editor">' \
            '<div style="width: 500px" class="django-ace-toolbar">' \
            '<a href="./" class="django-ace-max_min"></a>' \
            '</div>' \
            '<div class="django-ace-widget loading" ' \
            'style="width:500px; height:300px" ' \
            'data-showprintmargin data-use-worker data-usesofttabs>' \
            '<div></div>' \
            '</div>' \
            '<textarea name="name" rows="10" cols="40">\nvalue</textarea>' \
            '</div>'
        self.assertEqual(content, expected_content)

    def test_attrib(self):
        ace_widget = django_ace.AceWidget()
        expected_attrs = {
            'class': 'django-ace-widget loading',
            'style': 'width:500px; height:300px',
            'data-showinvisibles': False,
            'data-showprintmargin': True,
            'data-use-worker': True,
            'data-usesofttabs': True,
            'data-wordwrap': False,
        }
        self.assertEqual(ace_widget.get_attributes(), expected_attrs)

    def test_attrib_default(self, name='form-0-code', value='<html></html>'):
        ace_widget = django_ace.AceWidget()
        content = ace_widget.render(name, value)

        root = html5lib.parseFragment(content, namespaceHTMLElements=False)
        editor = root[0]
        self.assertEqual(len(editor), 3)
        self.assertEqual(editor.tag, 'div')
        self.assertEqual(editor.attrib['class'], 'django-ace-editor')

        toolbar = editor[0]
        self.assertEqual(toolbar.tag, 'div')
        self.assertEqual(sorted(toolbar.attrib.keys()), ['class', 'style'])
        self.assertEqual(toolbar.attrib['class'], 'django-ace-toolbar')
        self.assertEqual(toolbar.attrib['style'], 'width: 500px')
        self.assertEqual(toolbar[0].tag, 'a')
        self.assertEqual(sorted(toolbar[0].attrib.keys()), ['class', 'href'])
        self.assertEqual(toolbar[0].attrib['class'], 'django-ace-max_min')
        self.assertEqual(toolbar[0].attrib['href'], './')

        widget = editor[1]
        self.assertEqual(widget.tag, 'div')
        self.assertEqual(len(widget.attrib.keys()), 5)
        self.assertEqual(
            sorted(widget.attrib.keys()),
            sorted([
                'class',
                'style',
                'data-showprintmargin',
                'data-usesofttabs',
                'data-use-worker',
            ])
        )
        self.assertEqual(widget.attrib['class'], 'django-ace-widget loading')
        self.assertEqual(widget.attrib['style'], 'width:500px; height:300px')
        self.assertEqual(widget.attrib['data-showprintmargin'], '')
        self.assertEqual(widget.attrib['data-usesofttabs'], '')
        self.assertEqual(widget.attrib['data-use-worker'], '')

        textarea = editor[2]
        self.assertEqual(textarea.tag, 'textarea')
        self.assertEqual(textarea.attrib['name'], name)
        self.assertEqual(textarea.text, value)

    def test_attrib_no_toolbar(self, name='form-0-code', value='<html></html>'):
        ace_widget = django_ace.AceWidget(toolbar=False)
        content = ace_widget.render(name, value)

        root = html5lib.parseFragment(content, namespaceHTMLElements=False)
        editor = root[0]
        self.assertEqual(len(editor), 2)
        self.assertEqual(editor.attrib['class'], 'django-ace-editor')
        self.assertEqual(editor[0].tag, 'div')
        self.assertEqual(editor[0].attrib['class'], 'django-ace-widget loading')
        self.assertEqual(editor[1].tag, 'textarea')

    def test_attrib_no_worker(self, name='form-0-code', value='<html></html>'):
        ace_widget = django_ace.AceWidget(use_worker=False)
        content = ace_widget.render(name, value)

        root = html5lib.parseFragment(content, namespaceHTMLElements=False)
        editor = root[0]

        widget = editor[1]
        self.assertEqual(widget.tag, 'div')
        self.assertEqual(len(widget.attrib.keys()), 4)
        self.assertEqual(
            sorted(widget.attrib.keys()),
            sorted([
                'class',
                'style',
                'data-showprintmargin',
                'data-usesofttabs',
            ])
        )

    def test_attrib_options(self, name='form-0-code', value='<html></html>'):
        ace_widget = django_ace.AceWidget(
            mode='html',
            theme='twilight',
            wordwrap=True,
            showinvisibles=True,
            minlines=8,
            maxlines=16,
            tabsize=4,
            fontsize=12,
        )
        content = ace_widget.render(name, value)

        root = html5lib.parseFragment(content, namespaceHTMLElements=False)
        editor = root[0]

        widget = editor[1]
        self.assertEqual(widget.tag, 'div')
        self.assertEqual(len(widget.attrib.keys()), 13)
        self.assertEqual(
            sorted(widget.attrib.keys()),
            sorted([
                'class',
                'style',
                'data-mode',
                'data-theme',
                'data-wordwrap',
                'data-minlines',
                'data-maxlines',
                'data-tabsize',
                'data-fontsize',
                'data-showinvisibles',
                'data-showprintmargin',
                'data-usesofttabs',
                'data-use-worker',
            ])
        )
        self.assertEqual(widget.attrib['data-mode'], 'html')
        self.assertEqual(widget.attrib['data-theme'], 'twilight')
        self.assertEqual(widget.attrib['data-wordwrap'], '')
        self.assertEqual(widget.attrib['data-minlines'], '8')
        self.assertEqual(widget.attrib['data-maxlines'], '16')
        self.assertEqual(widget.attrib['data-tabsize'], '4')
        self.assertEqual(widget.attrib['data-fontsize'], '12')

    def test_attrib_size(self, name='form-0-code', value='<html></html>'):
        ace_widget = django_ace.AceWidget(width='90%', height='10em')
        content = ace_widget.render(name, value)

        root = html5lib.parseFragment(content, namespaceHTMLElements=False)
        editor = root[0]
        self.assertEqual(len(editor), 3)
        self.assertEqual(editor.tag, 'div')
        self.assertEqual(editor.attrib['class'], 'django-ace-editor')

        toolbar = editor[0]
        self.assertEqual(toolbar.tag, 'div')
        self.assertEqual(toolbar.attrib['class'], 'django-ace-toolbar')
        self.assertEqual(toolbar.attrib['style'], 'width: 90%')

        widget = editor[1]
        self.assertEqual(widget.tag, 'div')
        self.assertEqual(widget.attrib['class'], 'django-ace-widget loading')
        self.assertEqual(widget.attrib['style'], 'width:90%; height:10em')
