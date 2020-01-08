from django.http import HttpResponse,JsonResponse
from django.shortcuts import render

#def hello(request, arg1, arg2):#这里需要三个位置参数,arg1和arg2就代表url中的路由参数
#另外一种写法是*args,args可以随便命名,例如*a等等
def hello(request, *args):#这里的*args输出是元组,所以取值用args[0]等等
    '''
    #HttpResponse输出的是字符
    res = 'My name is {},Score is {}'.format(args[0], args[1])
    return HttpResponse(res)
    '''
    #JsonResponse输出的是字典
    res = {
        'desc':args[0],
        'score':args[1]
    }
    return JsonResponse(res)

# def user(request, *args):
#     res = {
#         'name':args[0],
#         'age':args[1]
#     }
#     return JsonResponse(res)

#表示关键字参数用**kwargs
def user(request, **kwargs):
    print(kwargs)
    PK = kwargs.get('PK')
    res = {
        'desc': '输入的PK值是: {}'.format(PK)
    }
    return JsonResponse(res)

#需求：通过sys接口执行linux命令:sys/ls -l
#例如执行pwd命令:http://x.x.x.x:8000/sys/pwd/
import os
def sys(request, **kwargs):
    cmd1 = kwargs.get('cmd')
    res = os.popen(cmd1)
    print(res)
    return HttpResponse(res)

def html(request, *args):
    arg = args[0]
    context = {
        'name' : arg
    }
    return render(request, 'sys.html', context)
