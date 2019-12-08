# import time
# def get_run():
#     start_time = time.time()
#     time.sleep(4)
#     print('hello')
#     end_time = time.time()
#     t = end_time - start_time
#     print(t)
#
# get_run()
#
# print("save")

#########################################
# def get_name(m,n):
#     print(m+n)
#     #注意:函数遇到return后,后面语句不再执行了
#     return(m+n)
#
# #return可以在调用的地方接收,这里的n就会传给a
# a = get_name(20,30)
# print(a)

#######################################
# 增加判断逻辑
# def get_run(m,n):
#     #判断逻辑一般的方法就是放在函数里面做
#     if type(m) == int and type(n) == int:
#         print(m+n)
#         #注意:函数遇到return后,后面语句不再执行了
#         return(m+n)
#     else:
#         print("parameter type error")
#
# #return可以在调用的地方接收,这里的n就会传给a
# a = get_run("aaa",30)
# print(a)

#####################################
#下面使用装饰器写一个对get_run函数的装饰器,用于检测m,n是不是int类型
def wap(func):
    def inner(*args, **kwargs):
        print("checked:", args, kwargs)
        #args是一个元组，所以需要将元组的值取出来
        m = args[0]
        n = args[1]
        if not (type(m) == int and type(n) == int):
            #return会结束掉内层函数inner
            return ("parameter type error")
        res = func(*args, **kwargs) #执行被装饰函数
        return res
    return inner

@wap
def get_run(m,n):
    print(m+n)
    #注意:函数遇到return后,后面语句不再执行了
    return(m+n)

#return可以在调用的地方接收,这里的n就会传给a
a = get_run("aaa",30)
print(a)

#装饰器最大的优点在于不需要修改被装饰函数的逻辑,逻辑可以写在装饰器里面


