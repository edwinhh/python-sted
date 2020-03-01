import time, django_redis, pickle
from django.views import View
from utils.custom_views import NbView, BaseView, PostView, GetView
from utils.tools import model_to_dict
from . import models, forms
from utils import const
from utils.custom_response import NbResponse
from utils.tools import md5


# 作业：
# 本地装好mysql 和 redis docker
# 开发页面的接口    仅限 get请求
# project、case、report、CaseCollection、 parameter（已完成）、interface
# Create your views here.
class LoginView(View):
    '''登录'''

    def post(self, request):
        user_form_obj = forms.LoginForm(request.POST)
        if user_form_obj.is_valid():
            user = user_form_obj.cleaned_data['user']
            token = '%s%s' % (user.username, time.time())
            token = md5(token)
            try:
                redis = django_redis.get_redis_connection()
            except:
                raise Exception("连接不上redis，请检查redis！")
            redis.set(const.token_prefix + token, pickle.dumps(user), const.token_expire)
            return NbResponse(token=token, user=user.username)
        else:
            return NbResponse(-1, user_form_obj.error_format)


class LogoutView(View):
    '''退出'''

    def post(self, request):
        redis = django_redis.get_redis_connection()
        print(dir(request))
        redis.delete(const.token_prefix + request.META.get('HTTP_TOKEN'))
        return NbResponse()


# 全局参数的接口。
class ParameterView(NbView):
    search_field = ["name"]  # 根据哪些字段来搜索
    filter_field = []  # 根据哪些字段来搜索
    model_class = models.Parameter  # 用哪个model类
    form_class = forms.ParameterForm  # 用哪个form类