#!/usr/bin/python
#coding: UTF-8
'''
Created on 2014年6月3日

@author: user
'''
#from  mysql.connector import connect
from wsgiref.simple_server import make_server 

from query import application
'''
def application(environ, start_response):  
    connection = connect(user='root', password='root', host='localhost', database='test')

    cursor = connection.cursor()
    cursor.execute("SELECT name FROM nametable ORDER BY name DESC LIMIT 10")
    
    output = "<html><head><title>Books</title><meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\"></head>\n"
    output += "<body>\n"
    output += "<h1>Books</h1>\n"
    output += "<ul>\n"

    # 取数查询结果数据
    for row in cursor.fetchall():
        output += "<li>%s</li>\n" % row[0]

    output += '<h2>environ的类型为：' + str(type(environ))[1:len(str(type(environ))) - 1] + '，内容如下：</h2>'
    
    environ.setdefault('MY_DEFINE', '自己定义')
    
    # 取environ变量的内容    
    for key, value in environ.items():
        output += "<li>%s: %s</li>\n" % (key, value)#.encode("utf-8")

    output += "</ul>\n"
    
    output += '<h2>start_response类型为: %s</h2>' % str(type(start_response))[1: len(str(type(start_response))) - 1]
    
    output += "</body></html>\n"

    connection.close()

    output = output.encode("utf-8")
    
    status = '200 OK'  
    response_headers = [('Content-type', 'text/plain'), ('Content-Length', str(len(output))), ('charset', 'utf-8')]  
    start_response(status, response_headers)

    return [output]  
'''
# Python自带的wsgiref模块简单的例子
httpd = make_server('', 8001, application)  
print("Serving on port 8001...")  

# Serve until process is killed  
httpd.serve_forever()
