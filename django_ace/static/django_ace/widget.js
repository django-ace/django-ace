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
        var divs = document.getElementsByClassName('django-ace-widget');

        for (var i = 0; i < divs.length; i++) {
            var div = divs[i];
            div.className = "django-ace-widget"; // remove `loading`
            var textarea = next(div),
                editor = ace.edit(div),
                mode = div.getAttribute('data-mode'),
                theme = div.getAttribute('data-theme');

            editor.getSession().setValue(textarea.value);

            // the editor is initially absolute positioned
            div.style.position = "relative";
            textarea.style.display = "none";

            if (mode) {
                var Mode = require("ace/mode/" + mode).Mode;
                editor.getSession().setMode(new Mode());
            }
            if (theme) {
                editor.setTheme("ace/theme/" + theme);
            }

            editor.getSession().on('change', function() {
                var value = editor.getSession().getValue();
                var textNode = document.createTextNode(value);
                textarea.innerHTML = "";
                textarea.appendChild(textNode);
            });
        }
    }

    if (window.addEventListener) { // W3C
        window.addEventListener('load', init);
    } else if (window.attachEvent) { // Microsoft
        window.attachEvent('onload', init);
    }
})();
