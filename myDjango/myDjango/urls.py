# -*- coding: UTF-8 -*-

from django.conf.urls import patterns, include, url

from django.contrib import admin
from myDjango.views import hello, current_datetime, hours_ahead, current_datetime1, current_datetime2, current_datetime3
from myDjango.views import current_datetime4, hours_ahead4


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^time1/$', current_datetime1),
    url(r'^time2/$', current_datetime2),
    url(r'^time3/$', current_datetime3),
    url(r'^time4/$', current_datetime4),
    url(r'^time4/plus/(\d{1,2})/$', hours_ahead4),
)
