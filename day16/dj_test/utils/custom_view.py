from django.db.models import Q
from django.views import View
from .custom_response import NbResponse
from django.forms import ModelForm
from django.db import models
from .const import page_limit
from django.core.paginator import Paginator
from .tools import model_to_dict

class BaseView(View):
    form_class = None
    model_class = None
    exclude = []
    field = []
    filter_field = [] #这个筛选用的字段
    search_field = [] #模糊查询用的字段

    @property
    def form(self):
        '''获取formclass的'''
        if not issubclass(self.form_class,ModelForm):
            raise Exception('form_class必须是一个modelform')
        return self.form_class

    @property
    def model(self):
        if not issubclass(self.model_class,models.Model):
            raise Exception('model_class必须是一个model')
        return self.model_class

    def get_paginator(self,data_list):
        try:
            page = int(self.request.GET.get('page', 1))
            limit = int(self.request.GET.get('limit', page_limit))
        except:
            page = 1
            limit = page_limit
        paginator = Paginator(data_list, limit)
        page_data = paginator.get_page(page)

        return page_data,paginator.count




    def get_filter_dic(self):
        filter_dic = {} #过滤的条件
        for field in self.filter_field:
            value = self.request.GET.get(field)
            if value:
                filter_dic[field] = value
        return filter_dic

    def get_search_obj(self):
        search = self.request.GET.get('search')
        search_field = ['name','desc']
        q = Q()
        if search:
            for field in search_field:
                d = {'%s__contains'%field : search }
                q = Q(**d)|q
        return q


class GetView(BaseView):
    def get(self, request):
        filter_dict = self.get_filter_dic()
        search_obj = self.get_search_obj()
        query_set = self.model.objects.filter(**filter_dict).filter(search_obj)
        page_data, count = self.get_paginator(query_set)

        data = []
        for c in page_data:
            d = model_to_dict(c, exclude=self.exclude, fields=self.field)  # 把查出来的每条数据转成字典
            data.append(d)

        return NbResponse(data=data, count=count)

class PostView(BaseView):
    def post(self, request):
        form = self.form(request.POST)  # name=xiaohei,desc=xxx
        if form.is_valid():
            form.save()  #
            return NbResponse()
        else:
            return NbResponse(-1,form.error_msg)

class DeleteView(BaseView):
    def delete(self,request):
        print('delete....')

        id = request.GET.get('id')
        # self.model.objects.filter(id=id).delete()
        self.model.objects.delete(id=id)
        return NbResponse()

class PutView(BaseView):
    def put(self,request):
        model_instance = self.model.objects.filter(id=request.PUT.get('id')).first()
        form = self.form(request.PUT,instance=model_instance)  #name=xiaohei,desc=xxx
        if form.is_valid():
            form.save()
            return NbResponse()
        #如果你要实现只传某个字段就修改某个字段的话，就拿着请求参数里面的key和出错的key做比较，如果请求的key没有出现
        #在出错的key里面就说明这个参数通过了校验
        else:
            return NbResponse(-1,form.error_msg)

class NbView(GetView,PostView,DeleteView,PutView):
    pass


