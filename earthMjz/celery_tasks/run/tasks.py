# 在celery中使用logger
import re

import django_redis
from celery.utils.log import get_task_logger
from utils.send_message import send_email
from sksystem import models
import json
from utils.http import MyRequest
from utils.response import ResponseCheck
from utils import const

logger = get_task_logger('django_server')

from celery_tasks.main import app


@app.task(name='async_send_mail')
def async_send_mail(*args, **kwargs):
    '''异步发送邮件，调用的时候使用 async_send_mail.delay(...)'''
    send_email(*args, **kwargs)


# @app.task(name='task_demo')
# def task_demo(case_id,user_id):
#     task_id = task_demo.request.id
#     print(task_id)
#     print(case_id)
#     print(user_id)
# class Run():
#     def __init__(self):
#         self.premise_id = []
#
#     def loop_case(self, case_id):
#         data = models.Case.objects.get(id=case_id).case.all()
#         for case in data:
#             self.premise_id.insert(0, case.premise_case.id)
#             if models.Case.objects.get(id=case.premise_case.id).case.all():
#                 self.loop_case(case.premise_case.id)
#         return self.premise_id
#
#     def get_all_case(self, cases_id):
#         for case_id in cases_id:
#             # 获取依赖用例
#             all_case = self.loop_case(case_id)
#             all_case.append(case_id)
#         print(all_case)
#         all_case_sort = list(set(all_case))
#         all_case_sort.sort(key=all_case.index)
#         return all_case_sort


class Run(object):
    '''
        提供执行单个用例的方法
        1、获取依赖用例
        2、运行方法

    '''

    def __init__(self):
        self.rely_cases = []
        self.redis = django_redis.get_redis_connection('redis2')

    def get_premise_case_id(self, case_id):
        # 获取当前用例的依赖用例
        case_obj = models.Case.objects.get(id=case_id)
        qs = case_obj.case.all()
        return qs

    def loop_premise(self, case_id):
        # A B   B C  C D ————》 依赖用例必须先执行  D C B A
        qs = self.get_premise_case_id(case_id)
        for item in qs:
            self.rely_cases.insert(0, item.premise_case.id)  # 依赖用例最先执行
            if self.get_premise_case_id(item.premise_case.id):
                self.loop_premise(item.premise_case.id)
        self.rely_cases.append(case_id)  # 最后将当前用例添加到用例列表

    def set_premise_case(self, case_ids):
        for case_id in case_ids:
            self.loop_premise(case_id)
        logger.debug('去重前的用例id-->%s' % self.rely_cases)
        # 如果要执行的用例重复：
        # 拖累你的执行时间
        # 去重时要保证原有顺序不发生改变
        all_case = list(set(self.rely_cases))
        # 当前列表  按照某个列表的顺序排列
        all_case.sort(key=self.rely_cases.index)
        logger.debug('去重后的用例id-->%s' % all_case)
        return all_case

    def data_replace(self, data):
        for k, v in data.items():
            keys = re.findall(r'\$\{(.*?)\}', str(v))
            if keys:
                # 如果keys存在 代表 有需要替换的参数 ['password']
                # 1、全局参数进行替换
                parameter_obj = models.Parameter.objects.filter(name=keys[0]).first()
                if parameter_obj:  # 如果全局参数存在则 取全局参数 否则 取缓存的
                    data[k] = parameter_obj.value
                else:
                    cache_value = self.redis.get(const.cache_prefix + keys[0])
                    data[k] = cache_value
        logger.debug('替换后的Data-->%s' % data)
        return data

    def set_cache(self, cache, response):
        caches = cache.split(',')
        for item in caches:
            item = item.replace(' ', '')
            res_cache_value = ResponseCheck.get_response_value(item, response)
            logger.debug('从返回值中获取的缓存字段-->:%s' % res_cache_value)
            self.redis.set(const.cache_prefix + item, res_cache_value, const.token_expire)

    def simple_run(self, case_id, task_id, user_id, collection_id=None):
        '''
            1、获取请求的各种信息
                如： 请求方式、url、接口、参数、header
            2、是否有${}格式的参数 需要替换
                a.怎么来判断字符串中窜在${}
                b.替换
            3、缓存
            4、报告  --
            5、更新用例状态


        :param case_id:
        :return:
        '''
        # 获取用例的对象
        case_obj = models.Case.objects.get(id=case_id)

        # 域名
        host = case_obj.project.host

        # 接口
        uri = case_obj.interface.uri

        # 请求方式
        method = case_obj.get_method_display()  # 通过get_method_display

        # 参数
        # 1、接口默认参数   case_obj.interface.params 取出实际是JSON串 str
        interface_params = json.loads(case_obj.interface.params) if case_obj.interface.params else {}
        # 2、用例的参数（以用例的为基准）
        case_params = json.loads(case_obj.params) if case_obj.params else {}

        # header
        # 1、接口的header
        interface_header = json.loads(case_obj.interface.headers) if case_obj.interface.headers else {}
        # 2 参数的header
        case_header = json.loads(case_obj.headers) if case_obj.headers else {}

        # is_json
        is_json = case_obj.is_json

        # json数据
        json_data = json.loads(case_obj.json) if case_obj.json else {}

        # 合并 参数 header  并且做替换
        # 将用例的header 覆盖 接口的
        interface_header.update(case_header)
        header = self.data_replace(interface_header)
        # 参数
        # json   kv 需要根据 is_json 状态来判断以谁为蓝本
        if is_json:
            interface_params.update(json_data)
        else:
            interface_params.update(case_params)
        data = self.data_replace(interface_params)

        logger.debug('url-->:%s' % host + uri)
        logger.debug('参数-->:%s' % data)
        logger.debug('header-->:%s' % header)
        logger.debug('method-->%s' % method)
        response = MyRequest(url=host + uri, method=method, data=data, is_json=is_json, headers=header).results
        logger.debug('接口返回值-->:%s' % response)

        # 验证接口返回值
        check = case_obj.check
        res = ResponseCheck(check, response)
        # 用例结果状态
        status = res.status
        # 原因
        reason = res.reason
        logger.debug('用例状态-->:%s' % status)
        logger.debug('原因-->:%s' % reason)
        # 如果用例结果为1 代表用例通过则缓存字段
        if status == 1:
            cache_field = case_obj.cache_field
            if cache_field:
                self.set_cache(cache_field, response)

        # 创建报告的数据结构
        create_data = {
            'response': str(response),
            'case': case_obj,
            'batch': task_id,
            'status': status,
            'duration': 100,
            'user': models.User.objects.get(id=user_id),
            'case_collection': models.CaseCollection.objects.get(id=collection_id) if collection_id else None,
            'reason': reason,
            'params': json.dumps(data),
            'url': host + uri,
            'title': case_obj.title,
            'project': case_obj.project,
        }
        models.Report.objects.create(**create_data)
        if collection_id:
            models.CaseCollection.objects.filter(id=collection_id).update(status=status)
        else:
            models.Case.objects.filter(id=case_id).update(status=status)


# 用例运行
@app.task(name='run_case')
def run_case(case_id, user_id):
    '''
    1、获取依赖用例
    2、运行 用例
    :param case_id:
    :param user_id:
    :return:
    '''
    task_id = run_case.request.id
    logger.debug("task_id-->%s" % task_id)
    # 1、获取依赖用例
    run = Run()
    all_case = run.set_premise_case([case_id])
    logger.debug('所有要运行的用例-->%s' % all_case)
    for case_id in all_case:
        run.simple_run(case_id, task_id, user_id)


# 集合运行
@app.task(name='run_collection')
def run_collection(collect_id, user_id):
    task_id = run_collection.request.id
    # 根据集合id 需要查找到集合下的所有用例id
    collection_obj = models.CaseCollection.objects.get(id=collect_id)
    qs = collection_obj.case.all()
    case_ids = []
    for item in qs:
        case_ids.append(item.id)  # 将集合下的用例 添加到列表中。
        # logger.debug('item-->%s'%item.id) # 13
    logger.debug('当前集合下真实的用例-->%s' % case_ids)
    # 以集合下的用例为基础，获取所有要运行的用例，也就是依赖用例
    run = Run()
    all_case = run.set_premise_case(case_ids)
    for case_id in all_case:
        run.simple_run(case_id,task_id,user_id,collect_id)

    # tmp_case = []
    # for case_id in case_ids:
    #     all_case = run.loop_premise(case_id)
    #     tmp_case += all_case
    # logger.debug("tmp_case-->%s"%tmp_case)
    # print(collection_case_id)
    # print("task_id", task_id)
    # print(collect_id)
    # print(user_id)

# def run(case_id):
#     '''单个用例原型'''
#     pass


#  获取依赖用例
# A B C
# A依赖于B B依赖于C  --- 》 真实情况 不清楚业务会配多少层依赖关系。
#
# 我们运行A。。。？？？？
