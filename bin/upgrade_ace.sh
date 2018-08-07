#!/bin/sh

git clone https://github.com/ajaxorg/ace-builds.git /tmp/ace
rsync --delete -r /tmp/ace/src/ django_ace/static/django_ace/ace/
