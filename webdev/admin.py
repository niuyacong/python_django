from django.contrib import admin
from .models import Question,Choice
# Register your models here.
# 向管理页面中加入投票应用


class ChoiceInline(admin.TabularInline):# admin.StackedInline
    model = Choice
    extra = 3
# 重新排列字段顺序
class QuestionAdmin(admin.ModelAdmin):
    # 1、 字段排序显示
    # fields=['pub_date','question_text']
    # 2、将表单分成几个数据集
    fieldsets=[
        (None,{'fields':['question_text']}),
        ('Date Info',{'fields':['pub_date'], 'classes': ['collapse']})
    ]
    inlines = [ChoiceInline]
    # 列表页显示
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # 列表右侧添加了一个过滤器 筛选制定字段
    list_filter = ['pub_date']
    # 制定搜索字段
    search_fields = ['question_text']

admin.site.register(Question,QuestionAdmin)

# admin.site.register(Choice)
# 创建管理员账号
# python manage.py createsuperuser
# 127.0.0.1:8000/admin
