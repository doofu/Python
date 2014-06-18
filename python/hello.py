#!/usr/bin/python
#coding: UTF-8

from httpUtil import httpResponse

def application(environ, start_response):  
	output = "<html><head><title>Books</title><meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\"></head>\n"
	output += "<body><h1>Hello World!</h1><br/><h3>可以通过此种方式反馈html页面</h3></body></html>\n"

	return httpResponse(start_response, output)

