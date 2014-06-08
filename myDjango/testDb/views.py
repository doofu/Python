#from django.shortcuts import render
from django.shortcuts import render_to_response
from testDb.models import Nametable
#from django.views.decorators.http import require_http_methods
from django.template import RequestContext

# 主菜单
def menu(request):
    return render_to_response('index.html')

def list_table(request):
    rec = Nametable.objects.get(name='add18')
#    return render_to_response('list_table.html', {'name': rec.name, 'age': rec.age, 'salary': rec.salary, 'phonenumber': rec.phonenumber, 
#                                                  'email': rec.email, 'password': rec.password, 'message': ' 数据库表内容显示！'})
    return render_to_response('list_table.html', {'rec': rec, 'message': ' 数据库表内容显示！'})

#@require_http_methods(["GET", "POST"])
def search(request):
    if request.method == 'GET':
        username = request.GET.get('username', '')
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
        