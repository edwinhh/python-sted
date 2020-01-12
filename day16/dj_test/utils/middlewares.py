from django.http import QueryDict
from django.utils.deprecation import MiddlewareMixin
from .custom_response import NbResponse
import traceback
from testcase.utils import Token
from django_redis import get_redis_connection
from testcase.const import session_pre
from .const import white_list
class PutMiddleware(MiddlewareMixin):

    def process_request(self,request):
        '''请求在走view之前会先走这里'''
        if 'multipart' in request.content_type:  # 判断是多媒体类型，也就可能传文件的
            data, files = request.parse_file_upload(request.META, request)
            request.PUT = data
            request._files = files
        else:
            request.PUT = QueryDict(request.body)

    def process_response(self,request,response):
        "view返回数据之后会走这里"
        print('process_response')
        return response

    def process_exception(self,request,exception):
        '''view里面出异常了会走这里'''
        print(traceback.print_exc())
        return NbResponse(-1,'未知错误')
        # print('process_exception')


class TokenMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # token = request.META.get('HTTP_TOKEN','')#从请求头里面
        for white in white_list:
            if white in  request.path_info:
                return

        token = request.GET.get("token")
        data = Token.check_token(token)
        if not data:
            return NbResponse(-3,'请登录！')
        r = get_redis_connection()
        redis_token = r.get(session_pre+data.get('username')).decode()

        if token == redis_token:
            request.user_info = data #给request里面加一个user的数据，方便以后使用
        else:
            return NbResponse(-2, '请登录！')






