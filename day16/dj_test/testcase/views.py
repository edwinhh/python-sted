from django.core.exceptions import ValidationError
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django import forms

from . import models


def case_set(request):
    # 添加用例集合
    name = request.POST.get('name')
    desc = request.POST.get('desc')
    if name.strip() and desc.strip():
        models.CaseSet.objects.create(name=name, desc=desc)
        data = {'code': 0, 'msg': '添加成功'}
    else:
        data = {'code': -1, 'msg': '参数错误'}
    return JsonResponse(data)


def case_set_all(req):
    case_sets = models.CaseSet.objects.filter(is_delete=False)

    data = []
    for c in case_sets:
        d = model_to_dict(c)
        data.append(d)
    response = {'code': 0, 'msg': '成功', 'data': data}

    return JsonResponse(response, json_dumps_params={'ensure_ascii': False})  # {'code': 0, 'msg': '成功',data:[ ]}


def case_set_new(req):
    if req.method == 'GET':
        case_sets = models.CaseSet.objects.filter(is_delete=False)
        data = []
        for c in case_sets:
            d = model_to_dict(c)
            data.append(d)
        response = {'code': 0, 'msg': '成功', 'data': data}
        return JsonResponse(response, json_dumps_params={'ensure_ascii': False})  # {'code': 0, 'msg': '成功',data:[ ]}
    elif req.method == 'POST':
        name = req.POST.get('name')
        desc = req.POST.get('desc')
        if name.strip() and desc.strip():
            models.CaseSet.objects.create(name=name, desc=desc)
            data = {'code': 0, 'msg': '添加成功'}
        else:
            data = {'code': -1, 'msg': '参数错误'}
        return JsonResponse(data)
    elif req.method == 'PUT':
        pass
    elif req.method=='DELETE':
        pass


class CaseSetForm(forms.ModelForm):
    class Meta:
        # fields = ['name','desc']
        exclude = ['is_delete']
        model = models.CaseSet


class CaseSet(View):

    def post(self,request):
        form = CaseSetForm(request.POST)
        if form.is_valid():
            form.save() #
            # models.CaseSet.objects.create(**form.cleaned_data)
            data = {'code': 0, 'msg': '添加成功'}
        else:
            print(form.errors.as_data())
            data = {'code': -1, 'msg': '参数错误'}
        return JsonResponse(data)

    def get(self,request):
        case_sets = models.CaseSet.objects.filter(is_delete=False)
        data = []
        for c in case_sets:
            d = model_to_dict(c)
            data.append(d)
        response = {'code': 0, 'msg': '成功', 'data': data}
        return JsonResponse(response, json_dumps_params={'ensure_ascii': False})

#form
class CaseForm(forms.Form):
    '''校验请求参数'''
    title = forms.CharField(max_length=50,min_length=2)
    desc = forms.CharField(max_length=60,required=False)
    method = forms.IntegerField() # 0 1 2 3
    url = forms.URLField()
    params = forms.CharField(max_length=100)

    def clean_method(self): #钩子
        method = self.cleaned_data.get('method')
        if method not in (0,1,2,3):
            raise ValidationError('method值不对')
        return  method

    def clean_title(self):#校验单个字段
        title = self.cleaned_data.get('title')
        if models.Case.objects.filter(title=title).count()>0:
            raise ValidationError('用例标题已经存在')
        return title

    def clean(self):#校验多个字段
        title = self.cleaned_data.get('title')
        method = self.cleaned_data.get('method')

class CaseForm2(forms.ModelForm):
    class Meta:
        # fields = '__all__' #代表所有字段
        exclude = ['case_set','run_count']
        model = models.Case



class CaseView(View):
    def post(self,request):
        # form = CaseForm(request.POST)
        form = CaseForm2(request.POST)
        if form.is_valid():
            print('这个是用了form校验的')
            models.Case.objects.create(**form.cleaned_data)
            data = {'code': 0, 'msg': '添加成功'}
        else:
            print(form.errors.as_data())
            data = {'code':-1,'msg':'参数错误'}
        return JsonResponse(data)

    def get(self,request):
        case_sets = models.Case.objects.filter(is_delete=False)
        data = []
        for c in case_sets:
            d = model_to_dict(c)
            data.append(d)
        response = {'code': 0, 'msg': '成功', 'data': data}
        return JsonResponse(response, json_dumps_params={'ensure_ascii': False})

    def delete(self,request):
        id = request.GET.get('id')
        models.Case.objects.filter(id=id).update(is_delete=True)
        response = {'code': 0, 'msg': '成功'}
        return JsonResponse(response, json_dumps_params={'ensure_ascii': False})

    def put(self,request):
        pass

