# -*- coding: utf-8 -*-
from django.contrib import admin
from django.db import models

from django_ace import AceWidget
from .models import Snippet


@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AceWidget(mode='html', theme='textmate')},
    }
