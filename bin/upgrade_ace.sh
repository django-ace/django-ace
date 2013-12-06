#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

git clone https://github.com/ajaxorg/ace-builds.git /tmp/ace
cd  "${DIR}/../django_ace/static/django_ace/ace"
cp -R /tmp/ace/src/* ./
