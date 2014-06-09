#from django.shortcuts import render
from django.shortcuts import render_to_response
from testDb.models import Nametable
#from django.views.decorators.http import require_http_methods
from django.template import RequestContext
from django.http import HttpResponse
import urllib.parse

#===============================================================================
# menu：主菜单
#===============================================================================
def menu(request):
    return render_to_response('index.html')

def list_table(request):
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
        return HttpResponse(xml)



