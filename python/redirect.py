#!/usr/bin/python
#coding: UTF-8
'''
Created on 2014年6月18日

@author: user
演示页面的跳转
'''
from httpUtil import httpRedirect

def application(environ, start_response):
    #return httpRedirect(start_response, '/query.py?redirect=true&from=redirect.py')
    url = '/query.py?redirect=true&from=redirect.py'
    status = '301 OK'  

    response_headers = [('Content-type', 'text/plain'), ('Content-Length', ''), ('Location', url)]  
    start_response(status, response_headers)  

    return [b'']


