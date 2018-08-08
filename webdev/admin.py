from django.contrib import admin
from .models import Question
# Register your models here.
# 向管理页面中加入投票应用
admin.site.register(Question)

# 创建管理员账号
# python manage.py createsuperuser
# 127.0.0.1:8000/admin
