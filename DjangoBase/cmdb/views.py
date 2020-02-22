from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import JsonResponse, QueryDict
from .models import *

# Create your views here.
class IdcView(TemplateView):
    template_name = 'cmdb/idcs.html'

    #使用post方法对数据库进行增加操作
    def post(self, request, *args, **kwargs):
        #获取数据
        data = QueryDict(request.body).dict()
        print(data)
        #写入到数据库
        Idc.objects.create(**data)
        return JsonResponse({})