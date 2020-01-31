###########################
#函数视图
###########################
# from django.http import HttpResponse,JsonResponse
# from django.shortcuts import render
#
# #def hello(request, arg1, arg2):#这里需要三个位置参数,arg1和arg2就代表url中的路由参数
# #另外一种写法是*args,args可以随便命名,例如*a等等
# def hello(request, *args):#这里的*args输出是元组,所以取值用args[0]等等
#     '''
#     #HttpResponse输出的是字符
#     res = 'My name is {},Score is {}'.format(args[0], args[1])
#     return HttpResponse(res)
#     '''
#     #JsonResponse输出的是字典
#     res = {
#         'desc':args[0],
#         'score':args[1]
#     }
#     return JsonResponse(res)
#
# # def user(request, *args):
# #     res = {
# #         'name':args[0],
# #         'age':args[1]
# #     }
# #     return JsonResponse(res)
#
# #表示关键字参数用**kwargs
# def user(request, **kwargs):
#     print(kwargs)
#     PK = kwargs.get('PK')
#     res = {
#         'desc': '输入的PK值是: {}'.format(PK)
#     }
#     return JsonResponse(res)
#
# #需求：通过sys接口执行linux命令:sys/ls -l
# #例如执行pwd命令:http://x.x.x.x:8000/sys/pwd/
# import os
# def sys(request, **kwargs):
#     cmd1 = kwargs.get('cmd')
#     res = os.popen(cmd1)
#     print(res)
#     return HttpResponse(res)
#
# def html(request, **kwargs):
#     cmd = kwargs.get('cmd')
#     res1 = os.popen(cmd)
#     context = {
#         'res1' : res1.read()
#     }
#     return render(request, 'sys.html', context)

###########################
#类视图
###########################
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
#导入基类模块
from django.views.generic import View, TemplateView
#导入如下模块可以将request请求的结果转换为字典
from django.http import request,QueryDict

#函数视图
def render_sys(request):
    return render(request, 'sys.html')

#类视图
class RenderSys(TemplateView):
    template_name = 'sys.html'
    #不写get方法,是因为父类里面已经有了
    #如果需要传递变量,只需要覆盖get_context_data方法即可
    def get_context_data(self, **kwargs):
        bio = 'qq we er rt tt ee'
        return {'bio': bio}

#定义类
class hello(View):
    def get(self, request, *args):
        it = [{'name':'Java', 'age':'30'}, {'name':'Python', 'age':31}, {'name':'JS', 'age':15}]
        users = ['user1','user2']
        bio = 'ww ee ee rr io po'
        context = {
            'name': args[0],
            'age':args[1],
            'it':it,
            'users':users,
            'bio':bio
        }
        return render(request, 'sys.html', context)
        #前端使用get请求
        #res = request.get(usl)
        #res.content

    def post(self, request, *args, **kwargs):
        #data = request.POST.get('n')#这样是QueryDict形式的
        #转化为字典
        #data = request.POST.dict()
        #或者
        data = QueryDict(request.body).dict()
        print(args, kwargs)#打印位置参数args及关键字参数kwargs
        print(data)
        #前端使用post请求,可以使用一个变量来接收
        #res = requests.post(url, data=data)
        #res.content
        #res.status_code
        return JsonResponse({'desc':data})

    #自定义方法,然后供get post put调用
    def handle_data(self, data):
        return data + '  123'

    def put(self, request, *args, **kwargs):
        data = QueryDict(request.body).dict()
        print(data)
        #调用handle_data方法
        res = self.handle_data('hahh')
        print(res)
        return JsonResponse({'desc':data, 'desc define': res})
        #前端使用put请求
        #res = requests.put(url, data=data)
#最后注意: 后端的方法和前端请求的方法需要对应起来。
#特别注意: get post put方法名称是不能变的,可以自定义方法进行数据处理,
#然后在get post put方法中调用它,例如上面的handle_data方法
    def delete(self, requests, *args, **kwargs):
        print(kwargs)#这里获取关键字参数pk的值
        return JsonResponse({})
        #前端使用delete请求
        #url = 'http://106.53.124.157:8000/hello/1/'
        #res = requests.delete(url)
#说明: restful风格
#       增删改查
#       get:一般是获取资源
#       post:一般是创建资源
#       put: 一般是修改资源（覆盖修改）
#       patch:一般是修改资源(部分修改)
#       delete:一般是删除资源

