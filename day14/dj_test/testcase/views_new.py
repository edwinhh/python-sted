from django.forms import model_to_dict
from django.http import JsonResponse
from django.core.paginator import Paginator
from . import models
from . import forms
from django.views import View
from django.db.models import Q

class CaseView(View):
    def post(self,request):
        form = forms.CaseForm(request.POST)
        if form.is_valid():
            models.Case.objects.create(**form.cleaned_data)
            data = {'code': 0, 'msg': '添加成功'}
        else:
            data = {'code':-1,'msg':form.error_msg}
        return JsonResponse(data)

    def get_paginator(self,data_list):
        limit = self.request.GET.get('limit',20)
        page = self.request.GET.get('page',1)
        paginator = Paginator(data_list, limit)
        page_data = paginator.page(page)
        return page_data,paginator

    def get_search_data(self):
        data = []
        search = self.request.GET.get('search')
        if search:
            data = models.Case.objects.filter(Q(title__contains=search) |
                                       Q(desc__contains=search) |
                                       Q(url__contains=search) |
                                       Q(params__contains=search)
                                       )
        return data


    def get_filter_data(self):
        data = []
        filter_field = ['id','title','method']#支持通过哪些字段来过滤
        filter_dict = {} #{'id':1,'title':abc}
        for field in filter_field: #
            value = self.request.GET.get(field)
            if value:
                filter_dict[field] = value
        if filter_dict:
            data = models.Case.objects.filter(**filter_dict)
        return data


    def get(self,request):
        if self.get_filter_data():
            case_sets = self.get_filter_data()
        elif self.get_search_data():
            case_sets = self.get_search_data()
        else:
            case_sets = models.Case.objects.filter(is_delete=False) #查询所有的
        page_data,paginator = self.get_paginator(case_sets)
        data = []
        for c in page_data:
            d = model_to_dict(c)
            data.append(d)
        response = {'code': 0, 'msg': '成功', 'data': data,'count':paginator.count}
        return JsonResponse(response, json_dumps_params={'ensure_ascii': False})

    def delete(self,request):
        id = request.GET.get('id')
        models.Case.objects.filter(id=id).update(is_delete=True)
        response = {'code': 0, 'msg': '成功'}
        return JsonResponse(response, json_dumps_params={'ensure_ascii': False})

    def put(self,request):
        pass

class CaseSet(View):

    def post(self,request):
        form = forms.CaseSetForm(request.POST)
        if form.is_valid():
            form.save() #
            # models.CaseSet.objects.create(**form.cleaned_data)
            data = {'code': 0, 'msg': '添加成功'}
        else:
            data = {'code': -1, 'msg': form.error_msg }
        return JsonResponse(data)

    def get(self,request):

        page = request.GET.get('page',1)
        limit = request.GET.get('limit',20)
        #1、模糊查询，哪写字段支持模糊查询 name、desc
        search = request.GET.get('search')

        #2、某些字段来过滤，id、name http://127.0.0.1:8000/case?id=1&name=abc&search=xxx

        filter_field = ['id','name'] #  #{id:1,name:2}
        filter_dic = {} #过滤的条件
        for field in filter_field:
            value = request.GET.get(field)
            if value:
                filter_dic[field] = value

        # case_sets = models.CaseSet.objects.filter(**filter_dic).filter(Q(name__contains=search)| Q(desc__contains=search)) #id=1,name=xx
        if search or filter_dic:  #1、只有search、只有filter、两种都有
            # case_sets = models.CaseSet.objects.filter(Q(name__contains=search) | Q(desc__contains=search))
            case_sets = models.CaseSet.objects.filter(**filter_dic).filter(
                Q(name__contains=search) | Q(desc__contains=search))  # id=1,name=xx

        else:
            case_sets = models.CaseSet.objects.filter(is_delete=False)


        paginator = Paginator(case_sets,limit)

        data = []
        for c in paginator.page(page):
            d = model_to_dict(c) #把查出来的每条数据转成字典
            data.append(d)

        response = {'code': 0, 'msg': '成功', 'data': data,'count':paginator.count}
        return JsonResponse(response, json_dumps_params={'ensure_ascii': False})
