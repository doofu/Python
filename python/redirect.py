#!/usr/bin/python
#coding: UTF-8
'''
Created on 2014年6月18日

@author: user
演示页面的跳转
'''
from httpUtil import httpRedirect

def application(environ, start_response):
    return httpRedirect(start_response, '/query.py?redirect=true&from=redirect.py')


