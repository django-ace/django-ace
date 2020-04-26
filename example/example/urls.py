# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib import admin

from .app.views import simple

urlpatterns = [
    url(r'^admin/?', admin.site.urls),
    url(r'', simple),
]
