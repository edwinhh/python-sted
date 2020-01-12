from django import forms
from django.core.exceptions import ValidationError
from utils.tools import FormatFormError
from . import models

from utils.tools import FormatFormError

class CaseSetForm(forms.ModelForm,FormatFormError):
    class Meta:
        model = models.CaseSet
        exclude = ['is_delete']
        # fields = ['name','desc']

class ProjectForm(forms.ModelForm,FormatFormError):
    class Meta:
        model = models.Project
        exclude = ['is_delete']


class CaseForm(forms.ModelForm,FormatFormError):
    class Meta:
        model = models.Case
        exclude = ['is_delete','case_set','run_count','run_time']




class CaseFormOld(forms.Form):
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


class UserForm(forms.Form,FormatFormError):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        u = models.User.objects.filter(username=username,password=password).first()
        if u:
            self.cleaned_data['u'] = u
        else:
            raise ValidationError('账号/密码错误！')

