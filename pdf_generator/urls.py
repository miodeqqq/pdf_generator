# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from core.views import GeneratePdf, HomeView

admin.autodiscover()

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^report/(?P<report_pk>\d+)/$', GeneratePdf.as_view(), name='generate_pdf'),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)