import datetime
from user.models import Category,Article
from django.shortcuts import render,HttpResponse

# Create your views here.


def index2(request):
    catagories = Category.objects.all()
    print (catagories)
    today = "22222"
    # return HttpResponse("哈哈哈哈")
    data = {'nav':catagories,'today1':today}
    return render(request,'index2.html',data)


def index(request):
    catagories = Category.objects.filter()
    article = Article.objects.filter(is_delete=False)
    data = {'nav':catagories,'articles':article}
    return render(request,'index.html',data)

def category(request,id):
    catagories = Category.objects.filter()
    article = Article.objects.filter(is_delete=False,category_id=id)
    data = {'nav':catagories,'articles':article}
    return render(request,'index.html',data)

