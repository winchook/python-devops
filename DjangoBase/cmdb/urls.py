from django.contrib import admin
from django.urls import path,re_path
from .views import * #这里的*表示导入所有的视图
#from .views import user,sys,html

urlpatterns = [
    re_path(r'idcs/$', IdcView.as_view()),
    re_path(r'idcs/(?P<pk>\d+)/$', IdcView.as_view()),
]