from django.http import JsonResponse


def NbResponse(code=0,msg='success',**kwargs):
    response = {'code':code,'msg':msg}
    response.update(kwargs)
    return JsonResponse(response,json_dumps_params={'ensure_ascii': False})


