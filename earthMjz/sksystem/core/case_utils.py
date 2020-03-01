# def get_premise_case(instance):
#     '''获取某个用例依赖的用例'''
#     premise_cases = []
#     premise_cases_qs = instance.case.all()  # 获取当前case依赖的所有用例，就是premise_case这个表的数据
#     for case in premise_cases_qs:
#         # 循环的时候取的是premise_case这个表里面的每一条数据，再根据外键获取到case的标题和id
#         premise_cases.append({"id": case.premise_case.id, "title": case.premise_case.title})
#     return premise_cases

from sksystem import models


def get_premise_case(instance):
    qs = instance.case.all()
    rely_cases = []
    for item in qs:
        rely_cases.append({"id": item.premise_case.id, "title": item.premise_case.title})
    print(rely_cases)
    return rely_cases


class Premise(object):
    def __init__(self):
        self.rely_cases = []

    def get_premise_case_id(self, case_id):
        case_obj = models.Case.objects.get(id=case_id)
        qs = case_obj.case.all()
        return qs

    def loop_premise(self, case_id, premise_id):
        # A B    B C  C A
        qs = self.get_premise_case_id(premise_id)
        self.rely_cases.append(premise_id)
        for item in qs:
            self.rely_cases.append(item.premise_case.id)  # 将依赖用例  所依赖的id 添加到列表
            if self.get_premise_case_id(item.premise_case.id):
                self.loop_premise(case_id, item.premise_case.id)
        return self.rely_cases


def check_premise(case_id, premise_id):
    '''
        # 检查当前用例 有没有被依赖用例所依赖。需要   当前用例id，依赖的用例id。
        # 检查是否被依赖的实现：
        #    1、被依赖的用例id中  有没有当前用例。如果有 代表递归了
        #    2、被依赖用例可能不直接依赖于当前用例，A B    B C  C A  递归解决。
                让递归结束的条件，最终一定会有一个用例 没有依赖。
    :param case_id:
    :param premise_id:
    :return:
    '''
    # 单程
    # case_obj = models.Case.objects.get(id=premise_id)
    # qs = case_obj.case.all()
    # rely_cases = []
    # for item in qs:
    #     rely_cases.append(item.premise_case.id)  # 将依赖用例  所依赖的id 添加到列表
    # print('依赖用例 所依赖的用例%s'%rely_cases)
    # print('当前用例->%s 数据类型->%s'%(case_id,type(case_id)))
    #
    # if int(case_id) in rely_cases:
    #     return False
    # else:
    #     return True

    # 递归
    premise = Premise()
    premise_ids = premise.loop_premise(case_id, premise_id)
    print('递归获取到的依赖用例%s' % premise_ids)
    if int(case_id) in premise_ids:
        return False
    else:
        return True
