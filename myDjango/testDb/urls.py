# -*- coding: UTF-8 -*-

from django.conf.urls import patterns, url

# 导入testDb应用的views
from testDb.views import list_table
from testDb.views import search, pythonAjax, ajaxSearch, pythonJQuery, jquerySearch, jqueryManage
from testDb.views import paging, pagingDisplay

urlpatterns = patterns('',
    url(r'^list/$', list_table),
    #url(r'^$', menu),
    url(r'^search/$', search),
    url(r'^pythonAjax/$', pythonAjax),
    url(r'^pythonAjax/ajaxSearch/$', ajaxSearch),
    url(r'^pythonJQuery/$', pythonJQuery),
    url(r'^pythonJQuery/jquerySearch/$', jquerySearch),
    url(r'^pythonJQuery/jqueryManage/(add|delete|modify)/$', jqueryManage),
#    url(r'^pythonJQuery/jqueryManage/(delete)/$', jqueryManage),
#    url(r'^pythonJQuery/jqueryManage/(modify)/$', jqueryManage),
    url(r'^paging/$', paging),
    url(r'^pagingDisplay/$', pagingDisplay),
)