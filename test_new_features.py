#!/usr/bin/env python
"""
Simple test script to verify the new vim keybinding and highlightActiveLine features
"""
import os
import sys

# Add django-ace to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Set up minimal Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_settings')

import django
from django.conf import settings

if not settings.configured:
    settings.configure(
        DEBUG=True,
        INSTALLED_APPS=[
            'django.contrib.contenttypes',
            'django.contrib.auth',
            'django_ace',
        ],
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        },
        USE_TZ=True,
    )
    django.setup()

from django import forms
from django_ace import AceWidget

# Test creating widgets with new parameters
print("Testing AceWidget with new parameters...")

# Test 1: Vim keybinding enabled
try:
    widget1 = AceWidget(
        mode="python",
        theme="monokai",
        vimKeyBinding=True,
        highlightActiveLine=True,
    )
    print("✓ Created widget with vimKeyBinding=True")
    assert widget1.vimKeyBinding == True
    assert widget1.highlightActiveLine == True
    print("✓ Parameters stored correctly")
except Exception as e:
    print(f"✗ Error creating widget with vim keybinding: {e}")

# Test 2: Highlight active line disabled
try:
    widget2 = AceWidget(
        mode="javascript",
        theme="twilight",
        vimKeyBinding=False,
        highlightActiveLine=False,
    )
    print("✓ Created widget with highlightActiveLine=False")
    assert widget2.vimKeyBinding == False
    assert widget2.highlightActiveLine == False
    print("✓ Parameters stored correctly")
except Exception as e:
    print(f"✗ Error creating widget: {e}")

# Test 3: Check media includes vim keybinding JS when enabled
try:
    widget_vim = AceWidget(vimKeyBinding=True)
    media = widget_vim.media
    js_files = media._js
    assert "django_ace/ace/keybinding-vim.js" in js_files
    print("✓ Vim keybinding JS file included in media when enabled")
except Exception as e:
    print(f"✗ Error checking media: {e}")

# Test 4: Check media doesn't include vim keybinding JS when disabled
try:
    widget_no_vim = AceWidget(vimKeyBinding=False)
    media = widget_no_vim.media
    js_files = media._js
    assert "django_ace/ace/keybinding-vim.js" not in js_files
    print("✓ Vim keybinding JS file not included when disabled")
except Exception as e:
    print(f"✗ Error checking media: {e}")

# Test 5: Check render output includes data attributes
try:
    widget = AceWidget(vimKeyBinding=True, highlightActiveLine=False)
    html = widget.render("test", "test value")
    assert 'data-vimkeybinding="true"' in html
    assert 'data-highlightactiveline="false"' in html
    print("✓ Render output includes correct data attributes")
except Exception as e:
    print(f"✗ Error checking render output: {e}")

print("\nAll tests completed!")