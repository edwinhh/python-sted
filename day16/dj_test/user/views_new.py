from utils.custom_view import NbView
from utils.custom_response import NbResponse
from utils.tools import model_to_dict
from .models import Article
from .froms import ArticleForm
class ArticleView(NbView):
    model_class = Article
    form_class = ArticleForm
    def get(self, request):
        filter_dict = self.get_filter_dic()
        search_obj = self.get_search_obj()
        query_set = self.model.objects.filter(**filter_dict).filter(search_obj)
        page_data, count = self.get_paginator(query_set)

        data = []
        for c in page_data:
            d = model_to_dict(c, exclude=self.exclude, fields=self.field)  # 把查出来的每条数据转成字典
            d['category_name'] = c.category.name
            d['category_id'] = c.category.id
            d.pop('category')
            data.append(d)

        return NbResponse(data=data, count=count)




