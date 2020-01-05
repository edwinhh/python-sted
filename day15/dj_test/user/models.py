from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(verbose_name='分类名称', max_length=50, unique=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    is_delete = models.BooleanField(verbose_name='是否删除', default=False)

    class Meta:  # 首页   5
        db_table = 'category'  #
        ordering = ['create_time']
        verbose_name = '文章分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name + '导航分类'


class Article(models.Model):
    title = models.CharField(verbose_name='文章标题', max_length=100, db_index=True)
    desc = models.CharField(verbose_name='描述', max_length=100, blank=True, null=True, default='这个文章没有描述')
    content = models.TextField(verbose_name='文章内容')
    img = models.ImageField(verbose_name='文章图片', upload_to='article_img',
                            default='images/1.jpg')  # 需要pip install pillow
    recommend = models.BooleanField(verbose_name='是否推荐', default=False)
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.DO_NOTHING,
                                 db_constraint=False)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    is_delete = models.BooleanField(verbose_name='是否删除', default=False)

    # models.CASCADE#guanl  cascade
    # db_constraint 不会真正在数据库里面建立外键
    class Meta:  # 首页   5
        db_table = 'article'  #
        ordering = ['-create_time']
        verbose_name = '文章'
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.title
