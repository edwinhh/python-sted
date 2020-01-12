from . import models

def category_process(request):
    categories = models.Category.objects.filter(is_delete=False)
    return  {'nav':categories}

def site_process(request):
    site_name = '王庆柱的博客'
    desc = "今天很困，一会要抽烟"
    return locals() #把当前函数里面的局部变量都返回
