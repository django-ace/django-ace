"""Run with: python -m unittest discover -s tests -v

Requires Django, Playwright, and its Chromium browser (development only).
Uses bundled assets and synthetic form data; no web server or network required.
"""

import unittest
from pathlib import Path

from django.conf import settings

if not settings.configured:
    settings.configure(
        SECRET_KEY="widget-test-only",
        INSTALLED_APPS=["django_ace"],
        TEMPLATES=[
            {
                "BACKEND": "django.template.backends.django.DjangoTemplates",
                "APP_DIRS": True,
            }
        ],
        STATIC_URL="/static/",
    )

import django

django.setup()

from django import forms
from django.template import Context, Template
from playwright.sync_api import sync_playwright

from django_ace import AceWidget

STATIC = Path(__file__).resolve().parents[1] / "django_ace" / "static"


class AutocompletionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch(headless=True)

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.playwright.stop()

    def test_independent_autocompletion_options(self):
        for basic, live in [(False, False), (True, False), (False, True), (True, True)]:
            with self.subTest(basic=basic, live=live):

                class EditorForm(forms.Form):
                    text = forms.CharField(
                        widget=AceWidget(
                            width=None,
                            height=None,
                            mode="python",
                            useworker=False,
                            basicautocompletion=basic,
                            liveautocompletion=live,
                        )
                    )

                form = EditorForm(initial={"text": "widget_value = 1\n"})
                html = Template("<form>{{ form.as_p }}</form>").render(
                    Context({"form": form})
                )
                scripts = "".join(
                    "<script>"
                    + (STATIC / asset)
                    .read_text(encoding="utf-8")
                    .replace("</script", "<\\/script")
                    + "</script>"
                    for asset in form.media._js
                )
                css = (STATIC / "django_ace/widget.css").read_text()
                with self.browser.new_context() as context:
                    context.route("**/*", lambda route: route.abort())
                    page = context.new_page()
                    page.set_default_timeout(3000)
                    errors = []
                    page.on("pageerror", lambda error: errors.append(str(error)))
                    page.set_content("<style>" + css + "</style>" + html + scripts)
                    result = page.evaluate("""() => {
                        const editor = document.querySelector('.django-ace-widget').editor;
                        const initial = editor.getValue();
                        editor.setValue('edited_widget_value = 2', -1);
                        return {
                            basic: !!editor.getOption('enableBasicAutocompletion'),
                            live: !!editor.getOption('enableLiveAutocompletion'),
                            initial,
                            posted: new FormData(document.querySelector('form')).get('text'),
                        };
                    }""")
                    self.assertEqual(errors, [])
                    self.assertEqual(result["initial"], "widget_value = 1\n")
                    self.assertEqual(result["posted"], "edited_widget_value = 2")
                    self.assertEqual(result["basic"], basic)
                    self.assertEqual(result["live"], live)
                    if live:
                        page.evaluate("""() => {
                            const editor = document.querySelector('.django-ace-widget').editor;
                            editor.navigateFileEnd();
                            editor.insert('\\n');
                            editor.focus();
                        }""")
                        page.keyboard.type("edited_widget")
                        page.wait_for_function("""() => {
                            const editor = document.querySelector('.django-ace-widget').editor;
                            return editor.completer && editor.completer.activated;
                        }""")
