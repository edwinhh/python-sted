from django.db import models

# Create your models here.

class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    is_delete = models.BooleanField(verbose_name='是否删除', default=False)
    class Meta:
        abstract = True #声明这个类只是用来继承的，不会创建这张表

class CaseSet(BaseModel):
    name = models.CharField(verbose_name='集合名称',max_length=60)
    desc = models.CharField(verbose_name='集合描述',max_length=70,blank=True)


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'case_set'
        verbose_name ='用例集合表'
        verbose_name_plural = verbose_name


class Case(BaseModel):
    title = models.CharField(verbose_name='用例标题',max_length=80,db_index=True,unique=True)
    desc = models.CharField(verbose_name='用例描述',max_length=120)
    method_choice = [
        [0,'get'],
        [1,'post'],
        [2,'put'],
        [3,'delete'],
    ]
    method = models.SmallIntegerField(choices=method_choice,verbose_name='请求方式',default=0)
    url = models.URLField(max_length=50,verbose_name='请求url')
    params = models.TextField(verbose_name='请求参数')
    run_count = models.IntegerField(verbose_name='运行次数',default=0,null=True,blank=True)
    run_time = models.DateTimeField(verbose_name='运行时间',null=True,blank=True)
    case_set = models.ManyToManyField(CaseSet,db_constraint=False,verbose_name='用例集合',null=True,blank=True)


    def __str__(self):
        return self.title

    class Meta:
        db_table = 'case'
        verbose_name ='用例表'
        verbose_name_plural = verbose_name



class Project(BaseModel):
    name = models.CharField(verbose_name='集合名称',max_length=60)
    desc = models.CharField(verbose_name='集合描述',max_length=70,blank=True)


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'project'
        verbose_name ='项目表'
        verbose_name_plural = verbose_name




class User(BaseModel):
    username = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'