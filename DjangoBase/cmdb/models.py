from django.db import models

# Create your models here.

class Idc(models.Model):
    '''
    机房表
    '''
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=32)
    remark = models.TextField()

    def __str__(self):#在python3用__str__代替__unicode__
        return self.name