# -*- coding: UTF-8 -*-

from django.conf.urls import patterns, include, url

from django.contrib import admin
# 导入myDjango应用的views
from myDjango.views import hello, current_datetime, hours_ahead, current_datetime1, current_datetime2, current_datetime3
from myDjango.views import current_datetime4, hours_ahead4
# 导入testDb应用的views
from testDb.views import menu
from testDb import urls

admin.autodiscover()

urlpatterns = patterns('',
    # 主菜单
    url(r'^$', menu),
    # myDjango应用的url
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^time1/$', current_datetime1),
    url(r'^time2/$', current_datetime2),
    url(r'^time3/$', current_datetime3),
    url(r'^time4/$', current_datetime4),
    url(r'^time4/plus/(\d{1,2})/$', hours_ahead4),
    # 在各自应用中定义url，在这里将testDb应用的urls包含进来
    url(r'^testdb/', include(urls)),
)
