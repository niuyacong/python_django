from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
"""
添加实体项
1、在项目的setting.py中INSTALLED_APPS添加配置项'webdev.apps.WebdevConfig',
2、运行 python manage.py makemigrations webdev(应用名称) 为模型的改变生成迁移文件 
3、运行 python manage.py migrate 来应用数据库迁移。

python命令行  实现database.api
python manage.py shell

from webdev import Choice,Quesion
获取所有数据
Question.objects.all()

from django,utils import timezone
插入数据
q=Question(question_text="what's new?",pub_date=timezone.now())
q.save()
获取值
q.id

更新值
q.question_text="what's up?"
q.save()

查询
Question.objects.filter(id=1)

Question.objects.filter(question_text__startswith="what")

current_year=timezone.now().year
Question.objects.get(pub_date__year=current_year)

Question.object.get(pk=1)

q=Question.objects.get(pk=1)
q.was_published_recently()

q.choice_set.all()
q.choice_set.create(choice_text='Not Much'，votes=0)
q.choice_set.count()

Choice.objects.filter(question_pub_date__yeat=cuttenr_year)

c=q.choice_set.filter(choice_text__startswith="No")
c.delete()
"""
class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now=timezone.now()
        return now-datetime.timedelta(days=1)<self.pub_date<=now
    was_published_recently.admin_order_field='pub_date'
    was_published_recently.boolean=True
    was_published_recently.short_description='Published recently?'
        
class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text