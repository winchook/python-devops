from django.http import HttpResponse,JsonResponse

#def hello(request, arg1, arg2):#这里需要三个位置参数,arg1和arg2就代表url中的路由参数
#另外一种写法是*args,args可以随便命名,例如*a等等
def hello(request, *args):#这里的*args输出是元组,所以取值用args[0]等等
    res = {
        'desc':args[0],
        'score':args[1]
    }
    return JsonResponse(res)