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
# 下面使用装饰器写一个对get_run函数的装饰器,用于检测m,n是不是int类型
# def wap(func):
#     def inner(*args, **kwargs):
#         print("checked:", args, kwargs)
#         #args是一个元组，所以需要将元组的值取出来
#         m = args[0]
#         n = args[1]
#         if not (type(m) == int and type(n) == int):
#             #return会结束掉内层函数inner
#             return ("parameter type error")
#         res = func(*args, **kwargs) #执行被装饰函数
#         return res
#     return inner
#
# @wap
# def get_run(m,n):
#     print(m+n)
#     #注意:函数遇到return后,后面语句不再执行了
#     return(m+n)
#
# #return可以在调用的地方接收,这里的n就会传给a
# a = get_run("aaa",30)
# print(a)


# 装饰器最大的优点在于不需要修改被装饰函数的逻辑,逻辑可以写在装饰器里面
########################################

# 装饰器第二个例子,计算程序运行时间
# import time
#
# def warp(func):
#     def inner(*args, **kwargs):
#         start_time = time.time()
#         res = func(*args, **kwargs)  # 执行装饰函数
#         end_time = time.time()
#         return res, end_time - start_time
#
#     return inner
#
# @warp
# def get_run():
#     time.sleep(2)
#     print('hello')
#     return 'running....'
#
#
# a = get_run()
# print(a)
##################################
#类的讲解
#属性:变量,方法:函数
#self是当前实例(对象)
#注意:定义了类Person,如果不去实例化它,这个类不会存在内存里面的
class Person:
    name = 'Jack'
    #init作用是初始化一些属性
    #传递参数有两种方式:
    #1,可以在公共的init中传递参数例如desc,传递变量在初始化时传入p=Person('地址')
    #2,可以在对应的方法get_desc中传递参数例如desc
    def __init__(self,address):#在实例化时候会去执行init初始化,然后在其他方法里就可以用这个score属性了
        self.score = 99
        self.address = address
    def get_desc(self,desc):
        return 'My name is {}, score is {}, {}, {}'.format(self.name, self.score, desc, self.address)
p = Person('shenzhen')
print(p.name)
print(p.get_desc('xxoo'))