from django.shortcuts import render,HttpResponse,Http404,HttpResponseRedirect
from django.http import JsonResponse
from django.views import View

from .models import Article,Category
from django.core.paginator import Paginator
from . import const
# Create your views here.

def index(request):
    category_id = request.GET.get('category_id',1) #?category_id=xx
    page = request.GET.get('page',1)
    limit = request.GET.get('limit',const.page_size)
    article = Article.objects.filter(is_delete=False,category_id=category_id)
    page_obj = Paginator(article,limit)
    page_data = page_obj.page(page)
    data = {'articles':page_data}
    return render(request,'index.html',data)

def detail(request):
    id = request.GET.get('id') #，参数在url里面的都用request.GET
    result = Article.objects.filter(id=id).first()
    return render(request, 'info.html', {'article':result})

def test(request):
    d = {'msg':'ok'}
    return  JsonResponse(d)


def xiake(request):
    s = '<h1 sityle="font-size:500px">哈哈哈</h1>'
    return render(request,'xiake.html',locals())


def add_article(request):
    if request.method=='GET':
        categories = Category.objects.all()
        return render(request,'form.html',locals())
    else:
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        category = request.POST.get('category')
        content = request.POST.get('content')
        article = Article(title=title,desc=desc,category_id=category,content=content)
        article.save()
        return HttpResponseRedirect('/index') #重定向

class ArticleView(View):

    def get(self,request):
        categories = Category.objects.all()
        return render(request, 'form.html', locals())

    def post(self,request):
        print('post请求...')
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        category = request.POST.get('category')
        content = request.POST.get('content')
        article = Article(title=title, desc=desc, category_id=category, content=content)
        article.save()
        return HttpResponseRedirect('/index')  # 重定向





