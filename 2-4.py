'''
#文件的操作
python2里面是file和open
python3里面只剩下open
'''
# #写文件
# filename = 'test.txt'
# f = open(filename, 'w')
# f.write('test111')
# f.close()
#
# #读文件
# f = open(filename)
# res = f.read()#read表示读取文件所有内容,readline表示读取一行结合while循环,防止读取大文件系统内存加载卡住
# f.close()
# print(res)
# ###############################
# #实例练习:
# #1,某字符出现的次数/每个字符出现的次数
# a = 'hello world'
# def check_str(s, strs):
#     n = 0
#     for i in strs:
#         if i == s:
#             n += 1
#     return n
# res = check_str('o', a)
# print(res)

# #使用字典实现统计每个字符的个数
# a = 'hello world'
# def check_str(s,strs):
#     d = {}
#     for i in strs:
#         if i not in d:
#             d[i] = 1
#         else:
#             d[i] += 1
#     return d
# res = check_str('o', a)
# print(res)

# #2,多种方法计算数列求和
# #方法一:内置的方法
# listn = range(101)
# print(sum(listn))
# #方法二:循环的法
# res = 0
# for n in listn:
#     res += n
# print(res)

# #3,访问日志分析(IP/URL/HTTP状态码等排序)
# filename = './a.txt'
# def handle_log():
#     f = open(filename)
#     res = {}#使用字典存放结果
#     while 1:
#         line = f.readline()
#         if not line:#如果读完了就退出
#             break
#         col = line.split()[0]#求客户端IP访问量,所以读取第一列,split默认按照空格进行切分
#         if col not in res:
#             res[col] = 1
#         else:
#             res[col] += 1
#         # i指res.items()转换后的元组,i[1]指出现的次数排序,reverse=True是从大到小排序
#         v = sorted(res.items(), key=lambda i:i[1] reverse=True)
#     print(v[:10]#取前10行
#     print(res)
# handle_log()

# #实现斐波那契数列(一组数列,从第三个数开始,每个数是前两个数之和)
# #例如:0 1 1 2 3 5 8 13 ...
# #用交换的思想实现
# a = 0
# b = 1
# n = 0
# while 1:
#     print(a)
#     a,b = b,a+b
#     if n == 10:
#         break
#     n += 1

