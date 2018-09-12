from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf import settings

urlpatterns = [
    url(r'^', include('app_modules.calculator.urls')),
    url(r'^admin/', admin.site.urls),
]

if settings.ALLOW_DT:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
