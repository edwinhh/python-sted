from django.shortcuts import render,HttpResponse,Http404
from django.http import JsonResponse
from .models import Article
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


