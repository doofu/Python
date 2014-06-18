#!/usr/bin/python
#coding: UTF-8
'''
Created on 2014年6月18日

@author: user

http工具包
'''
from urllib import parse

#===============================================================================
# httpResponse 显示html页面
#===============================================================================
def httpResponse(start_response, output):
    status = '200 OK' 
    
    output = output.encode(encoding='utf_8')
    
    response_headers = [('Content-type', 'text/plain'), ('Content-Length', str(len(output)))]  
    start_response(status, response_headers)
    
    return [output]

#===============================================================================
# httpRedirect 页面跳转
#===============================================================================
def httpRedirect(start_response, url):
    status = '301 OK'  

    response_headers = [('Content-type', 'text/plain'), ('Content-Length', ''), ('Location', url)]  
    start_response(status, response_headers)  

    return ['']

#===============================================================================
# getPostData 从environ中，取以POST方式上送的数据
#===============================================================================
def getPostData(environ):
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0

    # 当请求方法是POST的时候，查询字符串将从HTTP请求体中传递，这个请求体是由WSGI服务器传过来的类似于文件的wsgi.input环境变量中。
    request_body = environ['wsgi.input'].read(request_body_size)
    
    # 解析数据，放到字典中。字符为bytes类型的，因此需要转为utf-8
    request_data = parse.urlparse(request_body)
    postData = dict([x.split("=") for x in request_data.path.decode("utf-8").split("&")]) if (request_data.path) else {} # 返回一个字典
    
    # 对字符串进行URI解码，否则中文为乱码  
    for key in postData:
        postData[key] = parse.unquote(postData[key])
        
    return postData

#===============================================================================
# getGetData 从environ中，取以GET方式上送的数据
#===============================================================================
def getGetData(environ):
    request_data = parse.urlparse(environ['QUERY_STRING'])
    
    # 解析数据，放到字典中
    getData = dict([x.split("=") for x in request_data.path.split("&")]) if (request_data.path) else {}
    
    # 对字符串进行URI解码，否则中文为乱码            
    for key in getData:
        getData[key] = parse.unquote(getData[key])
        
    return getData