# -*- coding: UTF-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
import urllib.parse
from testDb.models import Nametable
from testDb.PagingToolbar import PagingToolbar
from testDb.ValidateCode import ValidateCode
import io

#===============================================================================
# login 用户登录
#===============================================================================
def login(request):
    if request.POST.get('checkNum', '') != request.session.get(('checkNum'), ''):
        errMessage = '验证码不正确' if request.POST.get('checkNum', '') else ''
        return render_to_response('login.html', {'errMessage': errMessage}, context_instance=RequestContext(request))
    
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    errMessage = ''
    
    try:
        response = HttpResponseRedirect('/')
        
        Nametable.objects.get(name=username, password=password)
        request.session['username'] = username          # 验证正确，设置session的username值
        
        # 判断是否选中保存用户名，并将是否选中状态保存到cookie中。如果选中，则在cookie中保存用户名，否则删除原来保存的用户名
        if request.POST.get('checked', ''):
            response.set_cookie('checked', 'checked')
            response.set_cookie('username', username)
        else:
            response.set_cookie('checked', '')
            response.set_cookie('username', '')
    except Exception:
        errMessage = '用户名不存在或密码不正确！'
        pass#
    finally:
        if request.session.get('username', ''):         # 如果验证已通过，自动重定向为主菜单
            return response
        else:                                           # 否则进入登录界面
            return render_to_response('login.html', {'errMessage': errMessage}, context_instance=RequestContext(request))

#===============================================================================
# checkNum 验证效验码
#===============================================================================
def checkNum(request):
    validateCode = ValidateCode()
    
    validateCode.createCheckNum()
    request.session['checkNum'] = validateCode.getCode()

    return HttpResponse(validateCode.toPicBuffer(), 'image/gif')

#===============================================================================
# logout 用户登出
#===============================================================================
def logout(request):
    del request.session['username']
    
    return HttpResponseRedirect('/login/')

#===============================================================================
# menu：主菜单
#===============================================================================
def menu(request):
    if not request.session.get('username', ''):
        return HttpResponseRedirect('/login/')
    else:
        return render_to_response('index.html', context_instance=RequestContext(request))

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
            # 处理数据库空值 
            pn = lambda x : x if x else '' 
                 
            rec = Nametable.objects.get(name=username)
            xml='<user><name>' + pn(rec.name) + '</name><age>' + str(pn(rec.age)) + '</age><salary>' + str(pn(rec.salary)) + '</salary>'
            xml = xml + '<phonenumber>' + pn(rec.phonenumber) + '</phonenumber><email>' + pn(rec.email) + '</email>'
            xml = xml + '<password>' + pn(rec.password) + '</password></user>'
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

#===============================================================================
# paging 演示分页类
#===============================================================================
def paging(request):
    data = {
            'request': request,
            'total_rows': 200,        # 总行数
            'method': 'get',          #导航方式：get
            'list_rows': 10,          #每页显示的行数，默认为15
            }
    page = PagingToolbar(data)
    get1 = page.show(1)
    get2 = page.show(2)
    data = {
        'request': request,
        'total_rows': 200,              # 总行数
        'method': 'ajax',               # 导航方式：ajax
        'ajax_func_name': 'ajaxfun',    # 使用Ajax或JQuery时，调用的javascript函数的名称
        'list_rows': 10,                # 每页显示的行数，默认为15
        }
    page = PagingToolbar(data)
    ajax3 = '<br/><br/>' + page.show(3)
    ajax4 = '<br/><br/>' + page.show(4)
    
    return render_to_response('html/pagingToolbarDemo.html', {'get1': get1, 'get2': get2, 'ajax3': ajax3, 'ajax4': ajax4})
        
#===============================================================================
# pagingDisplay 用分页类采用Get方式分页显示数据库表
#===============================================================================
def pagingDisplay(request):
    try:
        page_now = int(request.GET.get('p', '1'))
        total_rows = Nametable.objects.count()
        list_rows = 10
    
        records = Nametable.objects.all()[(page_now - 1) * list_rows : page_now * list_rows]
    except Exception as e:
        print(e)
    
    data = {
        'request': request,
        'total_rows': total_rows,       # 总行数
        'method': 'get',                #导航方式：get
        'page_name': 'p',
        'list_rows': list_rows,         #每页显示的行数，默认为15
        }
    pagingToolbar = PagingToolbar(data)
    
    return render_to_response('html/pythonPagingDisplay.html', {'records': records, 'total_rows': total_rows, 'pagingToolbar': pagingToolbar.show(1)})
    
#===============================================================================
# pagingDisplayJQueryPage JQuery分页显示页面显示
#===============================================================================
def pagingDisplayJQueryPage(request):
    now_page = int(request.GET.get('p', '1'))
    total_rows = Nametable.objects.count()
    list_rows = 10
    rowsCountList = range(0, list_rows)
    colsCountList = range(0, 6)
        
    data = {
        'request': request,
        'total_rows': total_rows,           # 总行数
        'now_page': now_page,               # 当前页
        'method': 'ajax', 'getPagingData'   # 导航方式：get
        'ajax_func_name': 'ajaxfun',        # 使用Ajax或JQuery时，调用的javascript函数的名称
        'page_name': 'p',
        'list_rows': list_rows,             #每页显示的行数，默认为15
        }
    pagingToolbar = PagingToolbar(data)
    
    return render_to_response('html/pythonPagingDisplayJQuery.html', {'list_rows': list_rows, 'total_rows': total_rows, 'rowsCountList': rowsCountList, 'colsCountList': colsCountList, 'pagingToolbar': pagingToolbar.show(4)})
    
#===============================================================================
# pagingDisplayJQuery JQuery访问服务，得到查询到的数据，以xml形式返回
#===============================================================================
def pagingDisplayJQuery(request):
    try:
        page_now = int(request.POST.get('pageNow', '1'))
        list_rows = int(request.POST.get('listRows', '1'))
    
        records = Nametable.objects.all()[(page_now - 1) * list_rows : page_now * list_rows]
    except Exception as e:
        print(e)
 
    # 处理数据库空值 
    pn = lambda x : x if x else ''        
    xml = '<users>'
    for rec in records:
        xml +='<user><name>' + pn(rec.name) + '</name><age>' + str(pn(rec.age)) + '</age><salary>' + str(pn(rec.salary)) + '</salary>'
        xml += '<phonenumber>' + pn(rec.phonenumber) + '</phonenumber><email>' + pn(rec.email) + '</email>'
        xml += '<password>' + pn(rec.password) + '</password></user>'
    xml += '</users>'

    return HttpResponse(xml)
        
#===============================================================================
# showPagingToolbar 分页工具条显示服务
#===============================================================================
def showPagingToolbar(request):
    now_page = int(request.POST.get('pageNow', '1'))
    total_rows = int(request.POST.get('totalRows', '1'))
    list_rows = int(request.POST.get('listRows', '1'))

    data = {
        'request': request,
        'total_rows': total_rows,               # 总行数
        'now_page': now_page,                   # 当前页
        'method': 'ajax',                       # 导航方式：get
        'ajax_func_name': 'getPagingData',      # 使用Ajax或JQuery时，调用的javascript函数的名称
        'parameter': str(list_rows) + ',' + str(total_rows),    # 自动调用javascript函数：ajax_func_name(当前页, 参数1, 参数2, ..., 参数n);
        'page_name': 'p', 
        'list_rows': list_rows,                 #每页显示的行数，默认为15
        }
    pagingToolbar = PagingToolbar(data)

    return HttpResponse(pagingToolbar.show(4))
    