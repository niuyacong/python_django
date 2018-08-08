
from django.http import HttpResponse
from django.shortcuts import render_to_response,get_object_or_404,render,HttpResponseRedirect
from django.template import loader
from django.http import Http404
import json
from .models import Question,Choice
from django.urls import reverse
from django.db.models import F
from django.views import generic
# Create your views here.

def index(request):
    last_question_list=Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('webdev/index.html')
    context = {
        'latest_question_list': last_question_list,
    }   
    # return HttpResponse(template.render(context,request))
    # 另一种方式
    return render(request,'webdev/index.html',context)


#error: TemplateDoesNotExist at /webdev/login
# 解决：setting.py TEMPLATES.'DIRS': [os.path.join(BASE_DIR,'templates')],
# error2:
# Forbidden (403)
# CSRF verification failed. Request aborted.
# 解决:'django.middleware.csrf.CsrfViewMiddleware', 注释掉
def login(request):
    if request.method =="GET":
        return render_to_response('login.html')# 此时页面路径 templates/login.html
    else:   
        username=request.POST.get('username')
        # 直接返回数据
        # return HttpResponse(username) 122
        result={}
        result['username']=username
        result=json.dumps(result)
        return HttpResponse(result,content_type="application/json;charset=utf-8")
        # {"username": "122"}


# 博客模块
# 详情页如果不存在，抛出404异常
def detail(request,question_id):
    # 如果不存在  则报404错误
    # try:
    #     question=Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # 另一种写法
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'webdev/detail.html',{'question':question})


def results(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'webdev/results.html',{'question':question})

def vote(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        return render(request,'webdev/detail.html',{'question':question,'error_message':"you did't vote a choice"})
    else:
        selected_choice.votes=F('votes')+1
        # 如果两个人同时操作，那么 selected_choice.votes+=1 只会执行一次
        # selected_choice.votes=F('votes')+1 两个人操作会执行两次
        selected_choice.save()
        return HttpResponseRedirect(reverse('webdev:results',args=(question.id,)))


# 配合urlconf 的通用视图写法
class IndexView(generic.ListView):
    template_name='webdev/index.html'
    context_object_name='latest_question_list'
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model=Question
    template_name='webdev/detail.html'

class ResultsView(generic.DetailView):
    model=Question
    template_name='webdev/results.html'