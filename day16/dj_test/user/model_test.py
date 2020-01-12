import django,os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj_test.settings')
django.setup()

from user.models import Category,Article
#增

# c_obj = Category.objects.create(name="Mysql1")#新增数据
# print(c_obj.name)
# print(c_obj.create_time)
# print(c_obj.update_time)

# obj = Category(name='Oracle')
# obj.save()

#查询
# Category.objects.all()#所有的
# obj = Category.objects.get(id=1)
# obj = Category.objects.get(id__gt=1)#大于
# obj = Category.objects.get(id__lt=1)#小于
# obj = Category.objects.get(id__gte=1)#大于等于
# obj = Category.objects.get(id__lte=1)#小于等于
#
# print(Category.objects.get(name="Mysql"))#获取一条
# data = Category.objects.filter(id__gte=1,name="首页")
# print(data.first())
# print(data.last())
# Category.objects.filter(name__endswith='xx')#以什么结尾
# Category.objects.filter(name__startswith='xx')#以什么开头
# Category.objects.exclude(name="首页").filter(id__gte=1) #不等于
# Category.objects.filter(name__startswith='李').exclude(sex="女")#连用
# print(Category.objects.filter(name__contains='L') )#包含
# print(Category.objects.filter(name__icontains='l'))#不区分大小写包含
# print(Category.objects.filter(name__in=['首页','Mysql','python']))

#or、!=、in、like  select * from xxx like '%李%';


#修改
# Category.objects.update(is_delete=True)#修改全表

# obj = Category.objects.get(id=1)#改某条数据
# obj.is_delete = False
# obj.save()

# Category.objects.filter(id__in=[2,3,4]).update(is_delete=False)

#删除

# Category.objects.all().delete()#删除全表
#
# obj = Category.objects.get(id=1)#改某条数据
# obj.delete()
# obj.save()
#
# Category.objects.filter(id__in=[2,3,4]).delete(is_delete=False)

# Category.objects.all().order_by("create_time")#排序

# c_obj = Category.objects.get(id=1) # 1->多
#
# print(c_obj.article_set.count())
# print(c_obj.article_set.all())
#
#
# #多
# article = Article.objects.get(id=1)
# print(article.category.name)

# l = range(1,51)

# from django.core.paginator import Paginator
#
# page_obj = Paginator(Article.objects.all(),2)
# print(list(page_obj.page(1)))
#
# print(page_obj.page(1)) #取某一页的数据
# print(page_obj.count) #总共多少条
# print(page_obj.num_pages) #总共分了多少页
#
# print(page_obj.page_range) #分页的范围
#
# cur_page = page_obj.page(1)
#
# print(cur_page.has_previous()) #判断是否有上一页
# #
# # print(cur_page.previous_page_number())
# print(cur_page.has_next())#判断是否有下一夜
# print(cur_page.next_page_number())
# print(cur_page.has_other_pages())
# print(cur_page.paginator)

# for  i in range(31):
#     article = Article(title='文章%s'%i,content="文章内容%s"%i)
#     article.category_id = 2
#     article.save()
# from django.db.models import Q
# # r = Article.objects.filter( Q(category_id=1) | Q(category_id=2) )
# # print(r)


from django_redis import get_redis_connection

# r = get_redis_connection()
import itsdangerous

key='sdgs2342$@13'

tjss = itsdangerous.TimedJSONWebSignatureSerializer(key,expires_in=20)
data  = {'user_id':1,'phone':18612532945}
# result = tjss.dumps(data)
# print(result.decode())

s='eyJhbGciOiJIUzI1NiIsImlhdCI6MTU3ODgyMDc0NywiZXhwIjoxNTc4ODIwNzY3fQ.eyJ1c2VyX2lkIjoxLCJwaG9uZSI6MTg2MTI1MzI5NDV9.aHtmf6MV8E2EIacITS81at61PEMi5kDK7SYBXuc4XSU'
# s = 'eyJhbGciOiJIUzI1NiIsImlhdCI6MTU3ODgyMDYwNSwiZXhwIjoxNTc4ODIxMTA1fQ.eyJ1c2VyX2lkIjoxLCJwaG9uZSI6MTg2MTI1MzI5NDV9.nEg8-3xx8ggQjG0ZbWwflhgYnGeyXr7k04GtTHuK5bI'
result = tjss.loads(s)
print(result)