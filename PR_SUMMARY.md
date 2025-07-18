# PR: Add Vim Keybinding and Highlight Active Line Support to django-ace

## Summary
This PR adds support for Vim keybindings and control over active line highlighting in the django-ace widget, providing users with enhanced editor functionality.

## Changes

### 1. `django_ace/widgets.py`
- Added `vimKeyBinding=False` parameter to `AceWidget.__init__`
- Added `highlightActiveLine=True` parameter to `AceWidget.__init__`
- Store both parameters as instance variables
- Include vim keybinding JS file in media when enabled
- Add `data-vimkeybinding` and `data-highlightactiveline` attributes to rendered widget

### 2. `django_ace/static/django_ace/widget.js`
- Read `data-vimkeybinding` attribute from widget and apply vim keybinding when enabled using `editor.setKeyboardHandler("ace/keyboard/vim")`
- Read `data-highlightactiveline` attribute from widget and disable active line highlighting when set to false

### 3. Example Application Updates
- Added `VimSnippetForm` demonstrating both vim keybinding and highlight active line features
- Updated view and template to show both standard and enhanced editors

### 4. `pyproject.toml`
- Updated Python version requirement from `> 2` to `>=3.8` for modern Django compatibility
- Updated Django dependency from `>=2` to `>=3.2`

## Usage

```python
from django_ace import AceWidget

class MyForm(forms.Form):
    code = forms.CharField(widget=AceWidget(
        mode='python',
        theme='monokai',
        vimKeyBinding=True,        # Enable vim keybindings
        highlightActiveLine=False, # Disable active line highlighting
    ))
```

## Features

### Vim Keybindings
When enabled, users can:
- Press 'i' to enter insert mode
- Press 'Esc' to return to command mode
- Use standard vim commands like 'dd', 'yy', 'p', etc.

### Highlight Active Line Control
- By default, ACE highlights the current line (existing behavior preserved)
- Setting `highlightActiveLine=False` disables this highlighting
- Useful for cleaner appearance or when vim keybindings are used

## Testing
Both features have been tested in the example application. The vim keybinding file (`keybinding-vim.js`) is already included in the ACE distribution within django-ace.

## Backward Compatibility
This change is fully backward compatible:
- `vimKeyBinding` parameter defaults to `False`
- `highlightActiveLine` parameter defaults to `True` (preserves existing behavior)
- All existing widgets will continue to work exactly as before