import datetime
from itertools import chain

from django.db.models.fields.files import ImageFieldFile


class FormatFormError:

    @property
    def error_msg(self):
        #优化错误信息提示
        msg = ''
        for error_key, value in self.errors.get_json_data().items():
            error_message = value[0].get('message')
            m = '%s:%s' % (error_key, error_message)
            msg += m
        return msg


def model_to_dict(instance, fields=None, exclude=None):  # 这个函数是我新加的
    """
    fields是返回哪些字段，exclude是排除哪些字段
    这个方法是参考了django自带的model_to_dict方法，做了修改，因为django自带的model转字典的方法
    日期类型的它不返回，所以改了一下，源码的位置在
    from django.forms.models import model_to_dict
    """
    opts = instance._meta  # 所有的字段
    data = {}
    for f in chain(opts.concrete_fields, opts.private_fields, opts.many_to_many):
        if fields and f.name not in fields:  # 判断传进来的字段是否在表里
            continue
        if exclude and f.name in exclude:  # 判断是否有排除的字段
            continue
        value = f.value_from_object(instance)
        if isinstance(value, datetime.datetime):
            #value = int(value.timestamp())
            value = value.strftime('%Y-%m-%d %H:%M:%S')
        if isinstance(value, datetime.date):
            value = value.strftime('%Y-%m-%d')
            #value = int(value.timestamp())
        if isinstance(value,ImageFieldFile):
            value = value.path
        data[f.name] = value
    return data