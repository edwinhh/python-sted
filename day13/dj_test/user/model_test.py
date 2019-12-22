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


#多表关联查询的时候，使用关联的模型类名要小写。（类型__属性名）
a = Article.objects.filter(category__name="linux")
for i in a:
    print(i.title)


b=Category.objects.get(name="test")
print(b.article_set.values())



article = Article.objects.get(id=1)
print(article.category.name)




#多
#article = Article.objects.get(id=1)



#c=Category.objects.create(name="new_one")
