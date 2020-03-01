from django.core.exceptions import ValidationError
from django.db.models import Q
from django.forms import ModelForm, Form
from django import forms

from . import models
from utils.tools import ExtendForm


class LoginForm(Form, ExtendForm):
    username = forms.CharField(min_length=5, max_length=20, required=True)
    password = forms.CharField(min_length=6, max_length=20, required=True)

    def clean(self):
        if not self.errors:  # 校验errors里面是否有错误
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            user = models.User.objects.filter(Q(phone=username) | Q(email=username))
            if user:
                user = user.first()
                if user.check_password(password):
                    self.cleaned_data['user'] = user
                    return self.cleaned_data
                else:
                    self.add_error('password', '密码错误')
            else:
                self.add_error('username', '用户不存在')


class ParameterForm(ModelForm, ExtendForm):
    class Meta:
        model = models.Parameter
        exclude = ['is_delete']


# 注册的form验证
class RegisterForm(ModelForm, ExtendForm):
    class Meta:
        model = models.User
        exclude = ['is_delete']


class ProjectForm(ModelForm, ExtendForm):
    class Meta:
        model = models.Project
        exclude = ['is_delete']


class InterfaceForm(ModelForm, ExtendForm):
    class Meta:
        model = models.Interface
        exclude = ['is_delete']


class CaseForm(ModelForm, ExtendForm):
    class Meta:
        model = models.Case
        exclude = ['is_delete', 'status']


class CaseCollectionFrom(ModelForm, ExtendForm):
    class Meta:
        model = models.CaseCollection
        exclude = ['is_delete', 'status','case']
