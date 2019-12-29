import datetime

from django.shortcuts import render,HttpResponse,Http404
from .models import Category,Article
# Create your views here.

def index(request):
    print('views...index')
    article = Article.objects.filter(is_delete=False)
    data = {'articles':article}
    return render(request,'index.html',data)

def category(request,id):
    article = Article.objects.filter(is_delete=False,category_id=id)
    data = {'articles':article}
    return render(request,'index.html',data)

def detail(request):
    id = request.GET.get('id')
    result = Article.objects.filter(id=id).first()
    return render(request, 'info.html', {'article':result})



