from django.contrib import admin
from testDb.models import Nametable

class NametableAdmin(admin.ModelAdmin):
    # ��ʾ�б��е��ֶ�
    list_display = ('name', 'age', 'salary', 'phonenumber', 'email', 'password')
    # ���������ֶ�
    search_fields = ('name', 'phonenumber', 'age')
    # ��ageɸѡ
    list_filter = ('age',)
    # ��name��С��������
    ordering = ('name',)
    # ����ɱ��༭���ֶΣ�name�����޸�
    fields = ('age', 'salary', 'phonenumber', 'email', 'password')

admin.site.register(Nametable, NametableAdmin)
#admin.site.register(Nametable)