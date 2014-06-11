# -*- coding: UTF-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
import urllib.parse
from testDb.models import Nametable
from testDb.PagingToolbar import PagingToolbar

#===============================================================================
# menu：主菜单
#===============================================================================
def menu(request):
    return render_to_response('index.html')

def list_table(request):
    print('request.get_full_path: ' + request.get_full_path())
    #print('request.path: ' + request.path())
    print('request.get_host: ' + request.get_host())
    print(type(request))

    rec = Nametable.objects.get(name='add18')
#    return render_to_response('list_table.html', {'name': rec.name, 'age': rec.age, 'salary': rec.salary, 'phonenumber': rec.phonenumber, 
#                                                  'email': rec.email, 'password': rec.password, 'message': ' 数据库表内容显示！'})
    return render_to_response('list_table.html', {'rec': rec, 'message': ' 数据库表内容显示！'})

def search(request):
    if request.method == 'GET':
        username = request.GET.get('username', '')  # 此处为何不需要url解码，中文仍然正常显示？
    else:
        username = request.POST.get('username', '')

    try:
        if username:       
            rec = Nametable.objects.get(name=username)
        else:
            rec = []
    except Exception:
        rec = [] 
    finally:
        return render_to_response('html/pythonMySql.html', {'rec': rec,}, context_instance=RequestContext(request))
        #return render_to_response('html/pythonMySql.html', {'rec': rec,})
        
def pythonAjax(request):
    return render_to_response('html/pythonAjax.html', context_instance=RequestContext(request))

#===============================================================================
# ajaxSearch: Ajax后台服务
#===============================================================================
def ajaxSearch(request):
    if request.method == 'GET':
        username = request.GET.get('username', '')
        username = urllib.parse.unquote(username)   #解决Get方式下中文乱码问题
    else:
        username = request.POST.get('username', '')
   
    try:
        if username:       
            rec = Nametable.objects.get(name=username)
            phonenumber = username + '的电话为：' + rec.phonenumber
        else:
            phonenumber = '未找到'
    except Exception:
        phonenumber = '未找到'
    finally:
        return HttpResponse(phonenumber)

def pythonJQuery(request):
    return render_to_response('html/pythonJQuery.html', context_instance=RequestContext(request))

#===============================================================================
# jquerySearch JQuery后台服务
#===============================================================================
def jquerySearch(request):
    if request.method == 'GET':
        username = request.GET.get('username', '')
        username = urllib.parse.unquote(username)   #解决Get方式下中文乱码问题
    else:
        username = request.POST.get('username', '')
    try:
        if username:       
            rec = Nametable.objects.get(name=username)
            xml='<user><name>' + rec.name + '</name><age>' + str(rec.age) + '</age><salary>' + str(rec.salary) + '</salary>'
            xml = xml + '<phonenumber>' + rec.phonenumber + '</phonenumber><email>' + rec.email + '</email>'
            xml = xml + '<password>' + rec.password + '</password></user>'
        else:
            xml = '<user><name></name><age></age><salary></salary><phonenumber></phonenumber><email></email><password></password></user>'
    except Exception:
        xml = '<user><name></name><age></age><salary></salary><phonenumber></phonenumber><email></email><password></password></user>'
    finally:
        print(xml)
        return HttpResponse(xml)
    
#===============================================================================
# jqueryManage 数据库增删改
#===============================================================================
def jqueryManage(request, op):
    if op == 'add':
        try:
            username = request.POST.get('username', '')

            if not(Nametable.objects.filter(name=username)):    # 当为找到时，filter不抛出异常，返回空列表
                age = int(request.POST.get('age', '0'))
                salary = float(request.POST.get('salary', '0.0'))
                phonenumber = request.POST.get('phonenumber', '')
                email = request.POST.get('email', '')
                password = request.POST.get('password', '')
                Nametable.objects.all()
                rec = Nametable(name=username, age=age, salary=salary, phonenumber=phonenumber, email=email, password=password)
                rec.save()
                ret = '增加成功！'
            else:
                ret = username + '已存在！！'
        except Exception as e:
            print(e)
            ret = '增加失败！！'
        finally:
            return HttpResponse(ret)
    elif op == 'delete':
        try:
            username = request.POST.get('username', '')

            rec = Nametable.objects.filter(name=username)    # 当为找到时，filter不抛出异常，返回空列表
            if rec:
                rec.delete()
                ret = '删除成功！'
            else:
                ret = '没有可删除的记录！！'  
        except Exception as e:
            ret = '删除失败！！'
        finally:
            return HttpResponse(ret)  
    elif op == 'modify':
        try:
            username = request.POST.get('username', '')
    
            if Nametable.objects.filter(name=username): 
                age = int(request.POST.get('age', '0'))
                salary = float(request.POST.get('salary', '0.0'))
                phonenumber = request.POST.get('phonenumber', '')
                email = request.POST.get('email', '')
                password = request.POST.get('password', '')
                Nametable.objects.all()
                rec = Nametable(name=username, age=age, salary=salary, phonenumber=phonenumber, email=email, password=password)
                rec.save()
                ret = '修改成功！'
            else:
                ret = username + '不存在！！'
        except Exception as e:
            print(e)
            ret = '修改失败！！'
        finally:
            return HttpResponse(ret)

def paging(request):
    data = {
            'request': request,
            'total_rows': 200,        # 总行数
            'method': 'get',          #导航方式：get
            'list_rows': 10,          #每页显示的行数，默认为15
            }
    page = PagingToolbar(data)
    html = page.show(1)
    html += '<br/><br/>' + page.show(2)
    data = {
        'request': request,
        'total_rows': 200,              # 总行数
        'method': 'ajax',               # 导航方式：ajax
        'ajax_func_name': 'ajaxfun',    # 使用Ajax或JQuery时，调用的javascript函数的名称
        'list_rows': 10,                # 每页显示的行数，默认为15
        }
    page = PagingToolbar(data)
    html += '<br/><br/>' + page.show(3)
    html += '<br/><br/>' + page.show(4)
    return HttpResponse(html)    
        
        