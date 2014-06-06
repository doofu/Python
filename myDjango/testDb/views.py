#from django.shortcuts import render
from django.shortcuts import render_to_response
from testDb.models import Nametable

def list_table(request):
    rec = Nametable.objects.get(name='add18')
#    return render_to_response('list_table.html', {'name': rec.name, 'age': rec.age, 'salary': rec.salary, 'phonenumber': rec.phonenumber, 
#                                                  'email': rec.email, 'password': rec.password, 'message': ' 数据库表内容显示！'})
    return render_to_response('list_table.html', {'rec': rec, 'message': ' 数据库表内容显示！'})

