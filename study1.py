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
# #类的讲解1
# #属性:变量,方法:函数
# #self是当前实例(对象)
# #注意:定义了类Person,如果不去实例化它,这个类不会存在内存里面的
# class Sport:
#     def get_desc(self,desc):
#         print('运动类型:{}'.format(desc))
# class Person:
#     name = 'Jack'
#     #init作用是初始化一些属性
#     #传递参数有两种方式:
#     #1,可以在公共的init中传递参数例如desc,传递变量在初始化时传入p=Person('地址')
#     #2,可以在对应的方法get_desc中传递参数例如desc
#     def __init__(self,address):#在实例化时候会去执行init初始化,然后在其他方法里就可以用这个score属性了
#         self.score = 99
#         self.address = address
#     def get_desc(self,desc):
#         return 'My name is {}, score is {}, {}, {}'.format(self.name, self.score, desc, self.address)
#
# class SportPerson(Person,Sport):#这里表示子类继承了父类Person,同时继承父类Sport
#     #写一个父类没有方法
#     age = 18
#     def run(self):
#         print('{} runing'.format(self.name))
#
#     #写一个与父类同样的方法,会覆盖父类的方法
#     # def get_desc(self):
#     #     print('descname {}'.format(self.name))
#
# #实例化子类
# sp = SportPerson('shanghai')
# #可以直接调用父类的方法
# #print(sp.get_desc('xxxx'))
# print(sp.get_desc('wwwwwwwww'))#用了子类的方法,没有传参
# print(sp.run())
#
# # p = Person('shenzhen')
# # print(p.name)
# # print(p.get_desc('xxoo'))
# #问题：
# #为什么要用类,可以全部用方法吗?是可以的,但是定义了类后就可以提高代码的复用率
# #相同的方法,覆盖优先级顺序子类>父类1>父类2
# #以上用到的全是实例方法
#######################################
# #类的讲解2
# #属性:变量,方法:函数
# #self是当前实例(对象)
# #注意:定义了类Person,如果不去实例化它,这个类不会存在内存里面的
# class Sport:
#     def get_desc(self,desc):
#         print('运动类型:{}'.format(desc))
# class Person:
#     name = 'Jack'
#     #init作用是初始化一些属性
#     #传递参数有两种方式:
#     #1,可以在公共的init中传递参数例如desc,传递变量在初始化时传入p=Person('地址')
#     #2,可以在对应的方法get_desc中传递参数例如desc
#     def __init__(self,address):#在实例化时候会去执行init初始化,然后在其他方法里就可以用这个score属性了
#         self.score = 99
#         self.address = address
#     #类方法的使用
#     @classmethod
#     def get_desc(cls,desc):
#         return 'My name is {} {}'.format(cls.name,desc)
#     #静态方法的使用
#     @staticmethod
#     def get_name():
#         print('========= {}'.format(Person.name))
#
# class SportPerson(Person,Sport):#这里表示子类继承了父类Person,同时继承父类Sport
#     #写一个父类没有方法
#     age = 18
#     def run(self):
#         print('{} runing'.format(self.name))
#
# #不需要实例化,直接调用
# print(SportPerson.get_desc('aaaaaaaaa'))
# #静态方法也不需要实例化
# SportPerson.get_name()
# #以上用到的是类方法
# #总结:实例方法/类方法/静态方法:
# #静态方法的使用中可以看出,我们不会访问到class本身,它基本上只是一个函数,
# #在语法上就像一个方法一样,但是没有访问对象和它的内部(字段和其他方法),
# #相反classmethod会访问cls,实例方法instancemethod会访问self
################################
# #1反射的讲解getattr
'''
Docstring:
getattr(object, name[, default]) -> value

Get a named attribute from an object; getattr(x, 'y') is equivalent to x.y.
When a default argument is given, it is returned when the attribute doesn't
exist; without it, an exception is raised in that case.
Type:      builtin_function_or_method
'''
# 示例1:
# class SportPerson:
#     age = 18
#     def run(self):
#         print('{} runing'.format(self.age))
# sp = SportPerson()
# res = getattr(sp, 'run')
# res()
# #应用场景:很多时候在许多框架中使用,将前端的请求GET/POST/DELETE等映射到后端

# #2反射的讲解setattr
'''
In [2]: setattr?
Signature: setattr(obj, name, value, /)
Docstring:
Sets the named attribute on the given object to the specified value.

setattr(x, 'y', v) is equivalent to ``x.y = v''
Type:      builtin_function_or_method

'''
# class SportPerson:
#     age = 18
#     def run(self):
#         print('{} runing'.format(self.age))
# sp = SportPerson()
# res = setattr(sp, 'run', '28')
# print(sp.run)

# #3反射的讲解hasattr
'''
In [3]: hasattr?
Signature: hasattr(obj, name, /)
Docstring:
Return whether the object has an attribute with the given name.

This is done by calling getattr(obj, name) and catching AttributeError.
Type:      builtin_function_or_method
'''
# class SportPerson:
#     age = 18
#     def run(self):
#         print('{} runing'.format(self.age))
# sp = SportPerson()
# res = hasattr(sp, 'run')
# print(res)
# #注意:最常用的是getattr
