from django.conf.urls import url
from django.contrib import admin
from .app.views import simple


urlpatterns = [
    url(r'', simple),
    url(r'^admin/', admin.site.urls)
]
