from django.contrib import admin
from testDb.models import Nametable

class NametableAdmin(admin.ModelAdmin):
    # 显示列表中的字段
    list_display = ('name', 'age', 'salary', 'phonenumber', 'email', 'password')
    # 可搜索的字段
    search_fields = ('name', 'phonenumber', 'age')
    # 按age筛选
    list_filter = ('age',)
    # 按name从小到大排序
    ordering = ('name',)
    # 定义可被编辑的字段，name不可修改
    fields = ('age', 'salary', 'phonenumber', 'email', 'password')

admin.site.register(Nametable, NametableAdmin)
#admin.site.register(Nametable)