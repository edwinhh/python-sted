from django.http import QueryDict
from django.utils.deprecation import MiddlewareMixin
from .custom_response import NbResponse
class PutMiddleware(MiddlewareMixin):

    def process_request(self,request):
        if 'multipart' in request.content_type:  # 判断是多媒体类型，也就可能传文件的
            data, files = request.parse_file_upload(request.META, request)
            request.PUT = data
            request._files = files
        else:
            request.PUT = QueryDict(request.body)

    def process_response(self,request,response):
        print('process_response')
        return response

    def process_exception(self,request,exception):
        print(exception)
        return NbResponse(-1,'未知错误')
        # print('process_exception')


