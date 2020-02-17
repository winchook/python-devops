from django.db import models

# Create your models here.

class Idc(models.Model):
    '''
    机房表
    '''
    name = models.CharField(max_length=32,null=True,blank=True)
    address = models.CharField(max_length=32)
    remark = models.TextField()
    price = models.CharField(max_length=64,null=True,blank=True,default='0')

    #这里表示是在Django后台显示的表,可有可无
    def __str__(self):#在python3用__str__代替__unicode__
        return self.name