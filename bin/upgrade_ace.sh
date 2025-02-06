#!/bin/sh

git clone https://github.com/ajaxorg/ace-builds.git /tmp/ace
rsync --delete -r /tmp/ace/src-min-noconflict/ django_ace/static/django_ace/ace/

echo "New ace version is:"
grep -o 'version="[^"]*"' django_ace/static/django_ace/ace/ace.js
