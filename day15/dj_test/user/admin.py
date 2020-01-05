from django.contrib import admin

# Register your models here.
from . import models

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'create_time', 'update_time'] #显示哪些字段
    search_fields = ['title'] #哪写字段可以搜索，不要写外键的字段
    list_filter = ['category','is_delete']
    list_per_page = 10 #每页显示多少条


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_time', 'update_time'] #显示哪些字段
    search_fields = ['name'] #哪写字段可以搜索，不要写外键的字段
    list_filter = ['is_delete']
    list_per_page = 10 #每页显示多少条



admin.site.register(models.Category,CategoryAdmin)
admin.site.register(models.Article,ArticleAdmin)



















