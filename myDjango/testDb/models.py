from django.db import models

# 使用命令行：python manage.py validate，检查语法
# 使用命令行：python manage.py sqlall testDb，生成创建数据库表的SQL语句。命令行中，testDb是app的名称。
# 使用命令行：python manage.py syncdb，创建数据库
# 使用命令行：python manage.py shell, Django带有一个命令行工具
class Nametable(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    phonenumber = models.CharField(max_length=20)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=10)
    # 如果没有指定该选项的话，Django会使用： app_label + '_' + model_class_name作为表名
    class Meta:
        db_table = 'Nametable'

    
    



 

