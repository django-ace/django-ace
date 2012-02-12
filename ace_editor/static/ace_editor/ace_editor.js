window.onload = function(){
    /**
     * Find all .ace-editor elements and set them in their respective modes.
     * */
    var editorWidgets = document.getElementsByClassName('ace-editor-widget');
    for(var i = 0, length = editorWidgets.length; i < length; i++){
        var editorWidget = editorWidgets[0];
        var editorElement = editorWidget.getElementsByClassName('ace_editor')[0];
        var editor = ace.edit(editorElement.id);
        editor.getSession().setUseSoftTabs(true);
        /**
         * This will probably be poorly performant as the input grows to move
         * the data on every keypress, a better solution could be to detect if
         * we are inside a form element and only serialize on submit.
         * */
         editor.getSession().on('change', function(){
            var value = editor.getSession().getValue();
            var textNode = document.createTextNode(value);
            var target = editorElement.getAttribute('data-target');
            var textarea = document.getElementById(target);
            textarea.innerHTML = "";
            textarea.appendChild(textNode);
        });
        var mode = editorElement.getAttribute('data-mode');
        if(mode){
            var Mode = require("ace/mode/" + mode).Mode;
            editor.getSession().setMode(new Mode());
        }
    }
};