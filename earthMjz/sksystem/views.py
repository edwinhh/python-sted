import time, django_redis, pickle
from django.views import View

from sksystem.core import case_utils
from utils.custom_views import NbView, BaseView, PostView, GetView
from utils.tools import model_to_dict
from . import models, forms
from utils import const
from utils.custom_response import NbResponse
from utils.tools import md5
from sksystem.core.case_utils import get_premise_case,check_premise
from celery_tasks.run.tasks import run_case, run_collection
import json

from utils.tools import qs_to_list
# 作业：
# 本地装好mysql 和 redis docker
# 开发页面的接口    仅限 get请求
# project、case、report、CaseCollection、 parameter（已完成）、interface
# Create your views here.
class LoginView(View):
    '''登录'''

    def post(self, request):
        user_form_obj = forms.LoginForm(request.POST)
        if user_form_obj.is_valid():
            user = user_form_obj.cleaned_data['user']
            print ('user.username:',user.username)
            token = '%s%s' % (user.username, time.time())
            token = md5(token)
            try:
                redis = django_redis.get_redis_connection()
            except:
                raise Exception("连接不上redis，请检查redis！")
            redis.set(const.token_prefix + token, pickle.dumps(user), const.token_expire)
            return NbResponse(token=token, user=user.username, user_id=user.id)
        else:
            return NbResponse(-1, user_form_obj.error_format)


class LogoutView(View):
    '''退出'''

    def post(self, request):
        redis = django_redis.get_redis_connection()
        print(dir(request))
        redis.delete(const.token_prefix + request.META.get('HTTP_TOKEN'))
        return NbResponse()


# 全局参数的接口。
class ParameterView(NbView):
    search_field = ["name"]  # 根据哪些字段来搜索
    filter_field = []  # 根据哪些字段来搜索
    model_class = models.Parameter  # 用哪个model类
    form_class = forms.ParameterForm  # 用哪个form类


class RegisterView(BaseView, PostView):
    '''注册需要md5加密在写入到数据库中'''
    model_class = models.User  # 用哪个model类
    form_class = forms.RegisterForm  # 用哪个form类

    def post(self, request):
        form_obj = self.form(request.POST)
        if form_obj.is_valid():
            # print(form_obj.cleaned_data)
            # md5加密
            md5_password = self.model.make_password(form_obj.cleaned_data['password'])
            # 更新原有的cleaned_data
            form_obj.cleaned_data['password'] = md5_password
            # 再创建
            # print(form_obj.cleaned_data)
            self.model.objects.create(**form_obj.cleaned_data)
            ret = NbResponse()  # 默认请求成功
        else:
            ret = NbResponse(code=-1, msg=form_obj.error_format)
        return ret


class ProjectView(NbView):
    search_field = ["name"]  # 根据哪些字段来搜索
    filter_field = []  # 根据哪些字段来搜索
    model_class = models.Project  # 用哪个model类
    form_class = forms.ProjectForm  # 用哪个form类

    def get(self, request):
        page_data, page_obj = self.get_query_set_page_data()  # 获取分页之后的数据
        data_list = []
        for instance in page_data:  #
            model_dict = model_to_dict(instance, self.fields, self.exclude_fields)  # 转成字典
            model_dict['user'] = instance.user.username
            data_list.append(model_dict)
        return NbResponse(data=data_list, count=page_obj.count)


class InterfaceView(NbView):
    search_field = ["name"]  # 根据哪些字段来搜索
    filter_field = ['project']  # 根据哪些字段来搜索
    model_class = models.Interface  # 用哪个model类
    form_class = forms.InterfaceForm  # 用哪个form类

    def get(self, request):
        page_data, page_obj = self.get_query_set_page_data()  # 获取分页之后的数据
        data_list = []
        for instance in page_data:  #
            model_dict = model_to_dict(instance, self.fields, self.exclude_fields)  # 转成字典
            model_dict['user'] = instance.user.username
            model_dict['project_name'] = instance.project.name
            model_dict['project_id'] = instance.project.id
            data_list.append(model_dict)
        return NbResponse(data=data_list, count=page_obj.count)


class CaseView(NbView):
    search_field = ["title"]  # 根据哪些字段来搜索
    filter_field = ['project']  # 根据哪些字段来搜索
    model_class = models.Case  # 用哪个model类
    form_class = forms.CaseForm  # 用哪个form类

    def get(self, request):
        page_data, page_obj = self.get_query_set_page_data()  # 获取分页之后的数据
        data_list = []
        for instance in page_data:  #
            model_dict = model_to_dict(instance, self.fields, self.exclude_fields)  # 转成字典
            model_dict['user'] = instance.user.username
            model_dict['project_name'] = instance.project.name
            model_dict['project_id'] = instance.project.id
            model_dict['interface_name'] = instance.interface.name
            model_dict['interface_id'] = instance.interface.id
            model_dict['rely_case'] = get_premise_case(instance)
            data_list.append(model_dict)
        return NbResponse(data=data_list, count=page_obj.count)

    # 由于需要创建依赖用例的自关联，所以需要重写post
    def post(self, request):
        form_obj = self.form(request.POST)
        # 从request.POST将用例依赖的case取出来
        rely_case = request.POST.get('rely_case')
        if form_obj.is_valid():
            # 想要进行自关联绑定，需要具备依赖用用例的id、以及自己的id
            case = self.model.objects.create(**form_obj.cleaned_data)
            # 绑定自关联 创建自关联关系
            for rely_case_id in json.loads(rely_case):
                models.CasePremise.objects.create(case_id=case.id, premise_case_id=rely_case_id)
            ret = NbResponse()  # 默认请求成功
        else:
            ret = NbResponse(code=-1, msg=form_obj.error_format)
        return ret

    def put(self, request):
        #  用例在更新时处理自关联的关系。
        # 先清掉之前所有的关联，然后在重新创建
        rely_case = request.PUT.get('rely_case')
        case_id = request.PUT.get('id')
        instance = self.model.objects.get(id=case_id)
        form_obj = self.form(request.PUT, instance=instance)
        if form_obj.is_valid():
            # 通过当前用例 获取所有被依赖的用例 并删除
            instance.case.all().delete()
            # 重新建立自关联绑定关系
            for item in json.loads(rely_case):
                # 检查当前用例 有没有被依赖用例所依赖。需要   当前用例id，依赖的用例id。
                # 检查是否被依赖的实现：
                #    1、被依赖的用例id中  有没有当前用例。如果有 代表递归了
                #    2、被依赖用例可能不直接依赖于当前用例，A B    B C  C A  递归解决。
                check_premise_status = check_premise(case_id,item) # true 或 false
                if check_premise_status: # 如果为真 代表没有被依赖的用例所依赖。可以创建依赖关系
                    models.CasePremise.objects.create(case_id=instance.id, premise_case_id=item)
                else:
                    return NbResponse(code=-1,msg='依赖用例存在递归，请查证。')
            form_obj.save()
            ret = NbResponse()  # 默认请求成功
        else:
            ret = NbResponse(code=-1, msg=form_obj.error_format)
        return ret


# 由于添加用例时，需要根据项目获取所有用例。因此开发/api/get_rely_case
class RelyCaseView(View):
    '''GET /api/get_rely_case?project_id=4 HT  如果不带case_id 说明是添加，只需要将项目下的用例返回
    /api/get_rely_case?project_id=4&case_id=7   # 如果带了caseid 说明是编辑，需要将这个case的依赖返回。
    1、项目下还没有用例   直接返回
    2、项目下已经有用例
        {
            "code": 0,
            "msg": "操作成功",
            "data": [
                {
                    "id": 2,
                    "title": "测试平台项目接口"
                },
                {
                    "id": 1,
                    "title": "测试平台登录接口"
                }
            ]
        }
    '''

    def get(self, requests):
        project_id = requests.GET.get('project_id')
        case_id = requests.GET.get('case_id')
        if case_id:
            # 编辑操作 当前这条用例不可以返回  通过exclude 进行过滤
            qs_data = models.Case.objects.filter(project_id=project_id, is_delete=1).exclude(id=case_id).values('id',
                                                                                                                'title')
        else:
            qs_data = models.Case.objects.filter(project_id=project_id, is_delete=1).values('id', 'title')
        return NbResponse(data=list(qs_data))


class CaseCollectionView(NbView):
    search_field = ["name"]  # 根据哪些字段来搜索
    filter_field = ['project']  # 根据哪些字段来搜索
    model_class = models.CaseCollection  # 用哪个model类
    form_class = forms.CaseCollectionFrom  # 用哪个form类
    exclude_fields = ['is_delete', 'case']  # 返回的时候排除哪些字段

    def get(self, request):
        page_data, page_obj = self.get_query_set_page_data()  # 获取分页之后的数据
        data_list = []
        for instance in page_data:  #
            model_dict = model_to_dict(instance, self.fields, self.exclude_fields)  # 转成字典
            model_dict['user'] = instance.user.username
            model_dict['project_name'] = instance.project.name
            model_dict['project_id'] = instance.project.id
            model_dict['case_count'] = instance.case.all().count()
            data_list.append(model_dict)
        return NbResponse(data=data_list, count=page_obj.count)


# http://127.0.0.1:8000/api/join_case?project_id=6&id=3

'''


'''


# 根据 项目和集合id 获取要选择的用例
class JoinCaseView(View):
    def get(self, request):
        '''
        #http://127.0.0.1:8000/api/join_case?project_id=6&id=3
{
    "code": 0,
    "msg": "操作成功",
    "data": {
        "all_case": [
            {
                "id": 2,
                "title": "测试平台项目接口"
            },
            {
                "id": 1,
                "title": "测试平台登录接口"
            }
        ],
        "join_case": [
            2,
            1
        ]
    }
}

        :param request:
        :return:

        1、根据项目id 返回当前项目下所有没有被删除的用例。
        2、根据集合id 获取已经和集合创建关系的用例id。
        '''
        project_id = request.GET.get('project_id')  # 项目id
        coll_id = request.GET.get('id')  # 集合id
        all_case = models.Case.objects.filter(project_id=project_id, is_delete=1).values('id', 'title')
        # 获取集合
        coll_obj = models.CaseCollection.objects.get(id=coll_id)
        # 通过多对多的查询获取集合下的用例 只要id字段
        join_case_qs = coll_obj.case.all().values('id')
        join_case = []  # 具体返回的joincase
        for item in join_case_qs:
            join_case.append(item.get('id'))
        data = {
            "all_case": list(all_case),
            "join_case": join_case
        }
        return NbResponse(data=data)

    def post(self, request):
        # http://127.0.0.1:8000/api/join_case
        '''
        join_case_list: [11,9,8,7]
        id: 3


        :param request:
        :return:
        '''
        join_case_list = request.POST.get('join_case_list')
        coll_id = request.POST.get('id')
        coll_obj = models.CaseCollection.objects.get(id=coll_id)
        # # 更新时第一种方案  清掉之前绑定的数据
        # coll_obj.case.clear()
        # for item in json.loads(join_case_list):
        #     coll_obj.case.add(item)
        # 第二种方案  通过 set的方式进行创建和更新
        coll_obj.case.set(json.loads(join_case_list))
        return NbResponse()


class CaseRunView(View):
    def post(self, request):
        case_id = request.POST.get('case_id')
        # user_id = request.POST.get('user_id')
        for item_id in json.loads(case_id):
            # 当页面调用异步任务时，会返回一个唯一的任务id
            task_id = run_case.delay(item_id, request.user.id)
            models.Case.objects.filter(id=item_id).update(report_batch=task_id, status=3)
        return NbResponse()


class CollectionRunView(View):
    def post(self, request):
        collect_id = request.POST.get('collect_id')
        # user_id = request.POST.get('user_id')
        for item_id in json.loads(collect_id):
            # 当页面调用异步任务时，会返回一个唯一的任务id
            task_id = run_collection.delay(item_id, request.user.id)
            models.CaseCollection.objects.filter(id=item_id).update(report_batch=task_id, status=3)
        return NbResponse()


class CaseReportView(View):
    # 用例报告中没有header字段，从report的数据表开始改起。--毕业作业
    def get(self, request):
        case_id = request.GET.get('id')
        report_batch = request.GET.get('report_batch')
        case = models.Case.objects.get(id=case_id)
        report = models.Report.objects.filter(batch=report_batch, case_id=case.id).first()
        if report:
            data = {
                'title': case.title,
                'run_time': report.create_time,
                'project_name': case.project.name,
                'status': report.status,
                'case_collection': report.case_collection if report.case_collection else '单用例运行',
                'duration': report.duration,
                'run_user': report.user.username,
                'url': report.url,
                'method': case.get_method_display(),
                'check': case.check,
                'reason': report.reason,
                'params': report.params,
                'response': report.response
            }
            return NbResponse(data=data)
        else:
            return NbResponse(-1, msg='用例运行中，请耐心等待..')


class CollectionReport(View):
    def get(self, request):
        case_collection_id = request.GET.get('id')
        report_batch = request.GET.get('report_batch')
        case_collection = models.CaseCollection.objects.get(id=case_collection_id)
        report = models.Report.objects.filter(batch=report_batch, case_collection=case_collection.id).first()
        fail_count = models.Report.objects.filter(batch=report_batch, case_collection=case_collection.id,
                                                  status=999).count()
        pass_count = models.Report.objects.filter(batch=report_batch, case_collection=case_collection.id,
                                                  status=1).count()
        if report:
            data = {
                'case_collection': case_collection.name,
                'run_time': report.create_time,
                'case_count': case_collection.case.all().count(),
                'pass_count': pass_count,
                'run_user': report.user.username,
                'fail_count': fail_count,
                'duration': 100,
                'report_batch': case_collection.report_batch,
            }
            return NbResponse(data=data)
        else:
            return NbResponse(-1, msg='用例集合运行中，请耐心等待..')




class ReportView(BaseView):
    search_field = ['title']
    filter_field = ['project', 'case_collection', 'batch']
    model_class = models.Report
    exclude_fields = ['is_delete']

    def get(self, request):
        page_data, page_obj = self.get_query_set_page_data()  # 获取分页之后的数据
        data_list = []
        for instance in page_data:  #
            model_dict = model_to_dict(instance, self.fields, self.exclude_fields)  # 转成字典
            model_dict['title'] = instance.case.title
            model_dict['project_name'] = instance.case.project.name
            model_dict['case_collection'] = instance.case_collection.name if instance.case_collection else '单用例运行'
            model_dict['status'] = instance.case.status
            model_dict['run_user'] = instance.user.username
            model_dict['run_time'] = instance.create_time
            model_dict['check'] = instance.case.check
            model_dict['method'] = instance.case.get_method_display()
            data_list.append(model_dict)
        return NbResponse(data=data_list, count=page_obj.count)



class HomePageView(View):
    def get_source_data(self, day):
        pass_count = models.Report.objects.filter(create_time__contains=day, status=1).count()
        fail_count = models.Report.objects.filter(create_time__contains=day, status=999).count()
        all_count = models.Report.objects.filter(create_time__contains=day).count()
        data = {
            "pass_count": pass_count,
            "fail_count": fail_count,
            "all_count": all_count
        }
        return data

    def get(self, request):
        import datetime
        today = datetime.date.today()
        # 统计数据 当天数据
        data = self.get_source_data(today)
        if models.HomeData.objects.filter(date=today).first():
            models.HomeData.objects.filter(date=today).update(**data)
        else:
            data.update({"date": today})
            models.HomeData.objects.create(**data)
        # 昨天数据

        yesterday = today - datetime.timedelta(days=1)
        data = self.get_source_data(yesterday)
        if models.HomeData.objects.filter(date=yesterday).first():
            models.HomeData.objects.filter(date=yesterday).update(**data)
        else:
            data.update({"date": yesterday})
            models.HomeData.objects.create(**data)

        # 最大执行次数和最大成功次数，用于确认页面的y轴数据
        max_all_count = models.Report.objects.all().count()
        max_pass_count = models.Report.objects.filter(status=1).count()

        project_count = models.Project.objects.filter(is_delete=1).count()
        interface_count = models.Interface.objects.filter(is_delete=1).count()
        collection_count = models.CaseCollection.objects.filter(is_delete=1).count()
        case_count = models.Case.objects.filter(is_delete=1).count()
        home_data = models.HomeData.objects.all().values()

        pass_count = qs_to_list(home_data, 'pass_count')
        date = qs_to_list(home_data, 'date')
        all_count = qs_to_list(home_data, 'all_count')
        fail_count = qs_to_list(home_data, 'fail_count')
        data = {
            'project_count': project_count,
            'interface_count': interface_count,
            'collection_count': collection_count,
            'case_count': case_count,
            'pass_count': pass_count,
            'date': date,
            'all_count': all_count,
            'fail_count': fail_count,
            'max_all_count': max_all_count,
            'max_pass_count': max_pass_count
        }
        return NbResponse(data=data)

