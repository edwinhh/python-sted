from django.http import QueryDict
from django.utils.deprecation import MiddlewareMixin
from utils.custom_response import NbResponse
from utils import const
from urllib.parse import unquote_plus, parse_qsl
from .settings import NO_LOGIN_LIST, DEBUG
import django_redis
import pickle


class PutMethodMiddleware(MiddlewareMixin):
    '''处理put请求，给request对象里面添加request.PUT'''

    @staticmethod
    def process_request(request):
        # 所有请求先走到这，然后再去请求视图
        contenttype = request.headers.get('Content-Type')
        if 'multipart' in contenttype:
            put_data,files = request.parse_file_upload(request.META,request)
            request.PUT = put_data
            request._files = files
        else:
            request.PUT = QueryDict(request.body)

class SessionMiddleware(MiddlewareMixin):
    '''校验token的中间件'''

    def check_uri(self, path):
        for uri in NO_LOGIN_LIST:  # 判断是uri否在白名单，在白名单的话，循环结束返回True
            if uri in path:
                return True
        return False

    def process_request(self, request):
        if not self.check_uri(request.path_info):  # 不在白名单，校验token
            token = request.META.get('HTTP_TOKEN')  # 从header里面获取token
            # token = request.GET.get('token')
            redis = django_redis.get_redis_connection()
            if token:
                user_bytes = redis.get(const.token_prefix + token)
                if user_bytes:
                    user = pickle.loads(user_bytes)  # 从redis里面获取到用户信息
                    request.user = user  # 加到request里面
                    request.token = token  # request里面添加token
                else:
                    return NbResponse(-1, '请登录！')
            else:
                return NbResponse(-1, '请登录！')


class ExceptionMiddleware(MiddlewareMixin):
    '''处理异常，不让接口接收到异常，有异常就返回系统异常'''

    def process_exception(self, request, exception):
        if not DEBUG:
            return NbResponse(500, '系统开小差了，请联系管理员 %s' % (exception))
