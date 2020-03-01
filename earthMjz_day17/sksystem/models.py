from django.db import models
from utils import tools
from earth import settings


# Create your models here.


class BaseModel(models.Model):
    '''公共字段'''
    is_delete_choice = (
        (0, '删除'),
        (1, '正常')
    )
    is_delete = models.SmallIntegerField(choices=is_delete_choice, default=1, verbose_name='是否被删除')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)  # auto_now_add的意思，插入数据的时候，自动取当前时间
    update_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)  # 修改数据的时候，时间会自动变

    class Meta:
        abstract = True  # 只是用来继承的,不会创建这个表


class User(BaseModel):
    '''用户表'''
    phone = models.CharField(verbose_name='手机号', max_length=11, unique=True)
    email = models.EmailField(verbose_name='邮箱', max_length=25, unique=True)
    password = models.CharField(verbose_name='密码', max_length=32)
    username = models.CharField(verbose_name='昵称', default='Python小学生', max_length=20)

    @staticmethod
    def make_password(raw_password):
        '''生成密码'''
        before_password = '%s%s' % (raw_password, settings.SECRET_KEY)  # 生成密码的算法，可以自己改
        after_password = tools.md5(before_password)
        return after_password

    def set_password(self, raw_password):
        '''设置密码'''
        self.password = self.make_password(raw_password)

    def check_password(self, raw_password):
        '''校验登录密码'''
        return self.make_password(raw_password) == self.password

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = verbose_name
        db_table = 'user'


class Parameter(BaseModel):
    '''全局参数表'''
    name = models.CharField(verbose_name='参数名', max_length=100, unique=True)
    desc = models.CharField(verbose_name='描述', max_length=200, null=True)
    value = models.CharField(verbose_name='参数值', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '全局参数'
        verbose_name_plural = verbose_name
        db_table = 'parameter'
        ordering = ['-id']  # 按照id倒排。


class Project(BaseModel):
    '''项目表'''
    name = models.CharField(verbose_name='项目名', max_length=100, unique=True)
    desc = models.CharField(verbose_name='描述', max_length=200, null=True)
    host = models.CharField(verbose_name='域名', max_length=1024)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_constraint=False, verbose_name='创建者')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '项目表'
        verbose_name_plural = verbose_name
        db_table = 'project'
        ordering = ['-id']  # 按照id倒排。


class Interface(BaseModel):
    '''接口'''
    name = models.CharField(verbose_name='接口名称', max_length=100, unique=True)
    uri = models.CharField(verbose_name='接口路径', max_length=1024)
    params = models.CharField(verbose_name='默认参数', max_length=2048,null=True,blank=True)
    headers = models.CharField(verbose_name='默认Headers', max_length=2048,null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_constraint=False, verbose_name='创建者')
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING, db_constraint=False, verbose_name='归属项目')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '接口表'
        verbose_name_plural = verbose_name
        db_table = 'interface'
        ordering = ['-id']  # 按照id倒排。


class Case(BaseModel):
    '''用例表'''
    title = models.CharField(verbose_name='用例标题', max_length=100)
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING, db_constraint=False, verbose_name='归属项目')
    interface = models.ForeignKey(Interface, on_delete=models.DO_NOTHING, db_constraint=False, verbose_name='接口')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_constraint=False, verbose_name='创建用户')
    method_choice = (
        (1, 'POST'),
        (2, 'GET'),
        (3, 'DELETE'),
        (4, 'PUT'),
    )
    method = models.SmallIntegerField(choices=method_choice, verbose_name='请求方式')

    cache_field = models.CharField(verbose_name='缓存字段', max_length=128, null=True, blank=True)

    check = models.CharField(verbose_name='校验点', max_length=512)
    params = models.CharField(verbose_name='请求参数', max_length=2048, null=True, blank=True)
    headers = models.CharField(verbose_name='请求头信息', max_length=2048, null=True, blank=True)
    is_json = models.BooleanField(verbose_name='参数是否是json', default=False)
    json = models.CharField(verbose_name='json类型参数', max_length=2048, null=True, blank=True)
    status_choice = (
        (1, '通过'),
        (2, '未运行'),
        (3, '运行中'),
        (999, '失败')
    )
    status = models.SmallIntegerField(choices=status_choice, verbose_name='用例状态',
                                      default=2)  # 记录上一次的状态 每次执行后需要更新下这个表的这个字段
    report_batch = models.CharField(verbose_name='最后一次执行的批次号', null=True, max_length=512, blank=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = '用例表'
        verbose_name_plural = verbose_name
        db_table = 'case'
        ordering = ['-id']  # 按照id倒排

class CaseCollection(BaseModel):
    '''用例集合'''
    name = models.CharField(verbose_name='集合名', max_length=100, unique=True)
    desc = models.CharField(verbose_name='描述', max_length=200, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_constraint=False, verbose_name='创建者')
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING, db_constraint=False, verbose_name='归属项目')
    report_batch = models.CharField(verbose_name='最后一次执行的批次号', null=True, max_length=512, blank=True)
    status_choice = (
        (2, '未运行'),
        (3, '运行中'),
        (4, '执行完毕')
    )
    status = models.SmallIntegerField(choices=status_choice, verbose_name='用例状态',
                                      default=2)
    case = models.ManyToManyField(Case,verbose_name='集合下的用例')


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = '用例集合表'
        verbose_name_plural = verbose_name
        db_table = 'case_collection'
        ordering = ['-id']  # 按照id倒排

class Report(BaseModel):
    '''用例报告表'''
    url = models.CharField(verbose_name='请求URL', max_length=1024)
    project = models.ForeignKey(Project, verbose_name='项目', on_delete=models.DO_NOTHING, db_constraint=False)
    title = models.CharField(verbose_name='用例名称', max_length=100)
    params = models.CharField(verbose_name='请求参数', max_length=2048)
    response = models.CharField(verbose_name='接口返回值结果', max_length=2048)
    case = models.ForeignKey(Case, on_delete=models.DO_NOTHING, db_constraint=False, verbose_name='结果所属用例')
    case_collection = models.ForeignKey(CaseCollection, on_delete=models.DO_NOTHING, db_constraint=False,
                                        verbose_name='结果所属集合', null=True)
    batch = models.CharField(verbose_name='批次', null=True, max_length=128)  # 用于区分运行的第几批集合的用例
    reason = models.CharField(verbose_name='失败原因', null=True, max_length=128, blank=True)
    status_choice = (
        (1, '通过'),
        (999, '失败')
    )
    duration = models.IntegerField(verbose_name='用例耗时')
    status = models.SmallIntegerField(choices=status_choice, verbose_name='用例结果状态')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_constraint=False, verbose_name='运行用户')

    class Meta:
        verbose_name = '用例报告表'
        verbose_name_plural = verbose_name
        db_table = 'report'
        ordering = ['-id']


class CasePremise(BaseModel):
    '''依赖用例的关系表'''
    case = models.ForeignKey(Case, verbose_name='用例id', on_delete=models.DO_NOTHING, db_constraint=False, unique=False,related_name='case')
    premise_case = models.ForeignKey(Case, verbose_name='被依赖用例的id', on_delete=models.DO_NOTHING, db_constraint=False,
                                     unique=False,related_name='premise_case')

    def __str__(self):
        return self.case

    class Meta:
        unique_together = ('case', 'premise_case')  # 联合主键，一个case对另外一个case只能依赖一次
        verbose_name = '依赖关系表'
        verbose_name_plural = verbose_name
        db_table = 'case_premise'



