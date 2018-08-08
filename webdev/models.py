from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
"""
添加实体项
1、在项目的setting.py中INSTALLED_APPS添加配置项'webdev.apps.WebdevConfig',
2、运行 python manage.py makemigrations webdev(应用名称) 为模型的改变生成迁移文件 
3、运行 python manage.py migrate 来应用数据库迁移。
"""
class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date>=timezone.now()-datetime.timedelta(days=1)
class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text