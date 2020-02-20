from django.db import models
#导入系统的用户表
from django.contrib.auth.models import User

# Create your models here.

class Idc(models.Model):
    '''
    机房表
    '''
    name = models.CharField(max_length=32,null=True,blank=True)
    address = models.CharField(max_length=32)
    remark = models.TextField()
    price = models.CharField(max_length=64,null=True,blank=True,default='0')

    def name_handle(self):
        return 'China_' + self.name

    #这里表示是在Django后台显示的表,可有可无
    #def __str__(self):#在python3用__str__代替__unicode__
    #    return self.name
    class Meta:
        ordering=['-id'] #结果按id降序排列
class Rack(models.Model):
    '''
    机柜表:一个机房有多个机柜，一个机柜有多台服务器
    那么，机房就是机柜的foreignkey
    '''
    #这里增加一个外键列,一个机房可能有多个机柜
    idc = models.ForeignKey(Idc,on_delete=models.SET_NULL,null=True,default='',related_name='IDC_RACK') #外键
    #on_delete参数设置方式
    #1,级联删除models.CASCADE:当关联表中的数据删除时,该外键也删除;
    #2,置空models.SET_NULL:当关联表中的数据删除时,该外键置空,当然,你的这个外键字段允许为空,null=True
    #3,models.SET_DEFAULT:当关联表中的数据删除时,外键设置为默认值,所以定义外键的时候注意加上一个默认值
    name = models.CharField(max_length=32,null=True,blank=True)

class Server(models.Model):
    '''
    服务器表:与开发人员表是多对多的关系
    '''
    name = models.CharField(max_length=32, null=True, blank=True)
    CPU = models.CharField(max_length=32, null=True)
    user = models.ManyToManyField(User, null=True, default='')
    #一个机柜可能有多个服务器
    rack = models.ForeignKey(Rack, on_delete=models.SET_NULL,null=True,default='',related_name='RACK_SERVER')