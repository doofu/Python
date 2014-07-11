#!/usr/bin/python
#coding: UTF-8
'''
Created on 2014年6月3日

@author: user
演示数据库访问，及http基本信息
可以自己定义一个request类，将关信息，封装到request类中。在其他地方，可以通过request对象，访问到有关信息
'''
from mysql.connector import connect
from httpUtil import getPostData, getGetData, httpResponse

def application(environ, start_response):  
    connection = connect(user='root', password='root', host='localhost', database='test')

    cursor = connection.cursor()
    cursor.execute("SELECT name FROM Nametable ORDER BY name DESC LIMIT 10")
    
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

    # 取POST和GET数据
    post_data = getPostData(environ)
    output += showData(post_data, 'POST数据：')
    
    get_data = getGetData(environ)
    output += showData(get_data, 'GET数据：')
    
    post_get_data = dict(post_data, **get_data)
    output += showData(post_get_data, 'POST和GET数据：')

    return httpResponse(start_response, output)  

def showData(data, msg):
    output = '<h3>%s</h2>' % msg
    for key in data:
        output += '<li>%s: %s</li>' % (key, data[key])
    
    return output
        