# -*- coding: UTF-8 -*-
'''
Created on 2014年6月5日

@author: user
'''

import datetime
# current_datetime1需要导入的包
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
# current_datetime2需要导入的包
from django.shortcuts import render_to_response

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

# 使用模板，手动导入
def current_datetime1(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

# 使用模板，便捷的方法！
def current_datetime2(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date': now, 'message': ' 便捷的模板方法！'})

# 没有像之前那样手工指定 context 字典，而是传入了 locals() 的值，它囊括了函数执行到该时间点时所定义的一切变量。
# locals() 并没有带来多大 的改进，但是如果有多个模板变量要界定而你又想偷懒，这种技术可以减少一些键盘输入。
# 调用 locals() 时，Python 必须得动态创建字典，因此它会带来一点额外的开销。如果手动指定 context 字典，则可以避免这种开销。
def current_datetime3(request):
    current_date = datetime.datetime.now()      # 变量名要改为模板中的名称
    message = '使用locals()'
    return render_to_response('current_datetime.html', locals())

# 使用模板的继承
def current_datetime4(request):
    now = datetime.datetime.now()
    return render_to_response('templates_extends/current_datetime.html', {'current_date': now, 'message': ' 模板的继承！'})

def hours_ahead4(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render_to_response('templates_extends/hours_ahead.html', {'hour_offset': offset, 'next_time': dt, 'message': ' 模板的继承！'})


