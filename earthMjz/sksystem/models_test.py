import django, os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'earth.settings')  # 设置django的配置文件
django.setup()

from sksystem import models

# 外键操作 的练习

# name、desc、host、user(外键)
# 创建含有外键的数据
# user_obj = models.User.objects.get(id=1)#"Project.user" must be a "User" instance.
# data = {
#     "name":"外键联系",
#     "desc":"描述",
#     "host":"http://127.0.0.1:8000",
#     "user":user_obj
# }
#
# models.Project.objects.create(**data)

# 外键的查询
# 正向查询
# project_obj = models.Project.objects.get(id=1)
# print(project_obj.user.nick)
#
#
# # 反向查询
# u_obj = models.User.objects.get(id=1)
# print(u_obj.project_set.all())


# 外键删除
# models.Project.objects.get(id=1).delete()

# 反向删除
# u_obj = models.User.objects.get(id=1)
# u_obj.project_set.all().delete()


#  外键自关联
# models.CasePremise.objects.create(case_id=1,premise_case_id=2)
#
# # 查询
# case_obj = models.Case.objects.get(id=1) # 获取id为1 的用例信息
#
# # CasePremise
# # case_obj.case.all() ==  select * from CasePremise where case_id= 1;
# qs = case_obj.case.all() # all() 返回的是一个列表的qs
#
# # [case_id为1的CasePremise数据]
#
# for item in qs: # qs实际是CasePremise的qs
#     # item 是CasePremise 依赖数据的对象
#     print(item.case.title)
#     print(item.premise_case.id)


# 多对多

# 用例集合 和 用例是多对多的关系
# A集合 和 B集合
# A用例 和 B用例
# A集合 -- A用例、B用例
# B集合 -- A用例、B用例
# ManyToMany

case_obj_A = models.Case.objects.get(id=1) # 获取用例A
case_obj_B = models.Case.objects.get(id=2) # 获取用例B
coll_obj = models.CaseCollection.objects.get(id=1) # 获取集合


# 通过集合中的case字段进行多对多的创建
# 创建多对多关系
# coll_obj.case.add(case_obj_B) # 通过add方法 创建多对多映射关系
# coll_obj.case.add(case_obj_A) # 通过add方法 创建多对多映射关系
coll_obj.case.add(1) # 创建时 通过id创建 也可以

# 查询多对多
# 正向 根据集合查集合下的用例
# print(coll_obj.case.all())
# # 反向 根据用例查所在集合
# print(case_obj_A.casecollection_set.all())

# 删除多对多关系
# coll_obj.case.clear()  # 清除掉所有和集合有关的用例关系
# coll_obj.case.remove(1) # 通过用例id 进行删除
# coll_obj.case.remove(case_obj_B) # 通过用例id 进行删除

# 更新
# coll_obj.case.set([2]) #将用例id为1和2的和集合建立关系