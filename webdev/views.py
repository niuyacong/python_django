from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
import json
# Create your views here.

def index(request):
    return HttpResponse("hello world,you are in webdev index")


#error: TemplateDoesNotExist at /webdev/login
# 解决：setting.py TEMPLATES.'DIRS': [os.path.join(BASE_DIR,'templates')],
# error2:
# Forbidden (403)
# CSRF verification failed. Request aborted.
# 解决:'django.middleware.csrf.CsrfViewMiddleware', 注释掉
def login(request):
    if request.method =="GET":
        return render_to_response('login.html')
    else:   
        username=request.POST.get('username')
        # 直接返回数据
        # return HttpResponse(username) 122
        result={}
        result['username']=username
        result=json.dumps(result)
        return HttpResponse(result,content_type="application/json;charset=utf-8")
        # {"username": "122"}