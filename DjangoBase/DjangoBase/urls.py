"""DjangoBase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from .views import * #这里的*表示导入所有的视图
#from .views import user,sys,html

urlpatterns = [
    path('admin/', admin.site.urls),

    #访问方式:http://193.112.2.124:8000/get_sys/
    re_path(r'get_sys/$', render_sys),

    #形如这样的访问http://0.0.0.0:8000/hello/a
    #这里的括号表示加参数传给hello这个函数,点代表一个字符,+代表多个字符
    #re_path(r'^hello/(.+)/(.+)$', hello.as_view()),
    #re_path(r'^user/(\w+)/(\d+)/$', user)
    #关键字参数如下表示,使用场景是给接口传递一个id
    #re_path(r'^user/(?P<PK>\d+)/$', user),#这里的PK在view里面也需要是PK
    #re_path(r'^sys/(?P<cmd>.+)/$', sys),
    #re_path(r'^html/(?P<cmd>.+)/$', html),
    re_path(r'^hello/(?P<pk>\d+)/$', hello.as_view()),

    #访问方式: http://106.53.124.157:8000/get_sys_func
    re_path(r'get_sys_func', render_sys),

    #访问方式: http://106.53.124.157:8000/get_sys_class
    re_path(r'get_sys_class', RenderSys.as_view()),

    #如下表示当浏览器访问包含cmdb链接时,将路由转至cmdb应用下的urls文件
    path('cmdb/', include('cmdb.urls'))
]
