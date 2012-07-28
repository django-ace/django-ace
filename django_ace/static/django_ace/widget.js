(function() {
    function next(elem) {
        // Credit to John Resig for this function
        // taken from Pro JavaScript techniques
        do {
            elem = elem.nextSibling;
        } while (elem && elem.nodeType != 1);
        return elem;
    }

    function init() {
        var widgets = document.getElementsByClassName('django-ace-widget');

        for (var i = 0; i < widgets.length; i++) {
            var widget = widgets[i];
            widget.className = "django-ace-widget"; // remove `loading` class

            var div = widget.firstChild,
                textarea = next(widget),
                editor = ace.edit(div),
                mode = widget.getAttribute('data-mode'),
                theme = widget.getAttribute('data-theme'),
                wordwrap = widget.getAttribute('data-wordwrap');

            editor.getSession().setValue(textarea.value);

            // the editor is initially absolute positioned
            textarea.style.display = "none";

            // options
            if (mode) {
                var Mode = require("ace/mode/" + mode).Mode;
                editor.getSession().setMode(new Mode());
            }
            if (theme) {
                editor.setTheme("ace/theme/" + theme);
            }
            if (wordwrap == "true") {
                editor.getSession().setUseWrapMode(true);
            }

            editor.getSession().on('change', function() {
                textarea.value = editor.getSession().getValue();
            });
        }
    }

    if (window.addEventListener) { // W3C
        window.addEventListener('load', init);
    } else if (window.attachEvent) { // Microsoft
        window.attachEvent('onload', init);
    }
})();
