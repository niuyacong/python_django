from django.urls import path
from . import views


# 为url添加命令空间
app_name = 'webdev'
# 同样的 webdev/templates/webdev/index.html 中指向name为detail的url 也要进行修改

# 第一版常规操作
# urlpatterns=[
#     path('',views.index,name='index'),
#     path('login',views.login,name='login'),
#     path('<int:question_id>/results/',views.results,name="results"),
#     path('<int:question_id>/',views.detail,name="detail"),
#     path('<int:question_id>/vote/',views.vote,name="vote")
# ]
# 第二版 改为通用模板
urlpatterns=[
    path('',views.IndexView.as_view(),name='index'),
    path('login',views.login,name='login'),
    path('<int:pk>/results/',views.ResultsView.as_view(),name="results"),
    path('<int:pk>/',views.DetailView.as_view(),name="detail"),
    path('<int:question_id>/vote/',views.vote,name="vote")
]