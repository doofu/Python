# -*- coding: UTF-8 -*-

from django.conf.urls import patterns, include, url

from django.contrib import admin
from myDjango.views import hello, current_datetime, hours_ahead


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
)
