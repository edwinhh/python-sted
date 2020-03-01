# def get_premise_case(instance):
#     '''获取某个用例依赖的用例'''
#     premise_cases = []
#     premise_cases_qs = instance.case.all()  # 获取当前case依赖的所有用例，就是premise_case这个表的数据
#     for case in premise_cases_qs:
#         # 循环的时候取的是premise_case这个表里面的每一条数据，再根据外键获取到case的标题和id
#         premise_cases.append({"id": case.premise_case.id, "title": case.premise_case.title})
#     return premise_cases


def get_premise_case(instance):
    qs = instance.case.all()
    rely_cases = []
    for item in qs:
        rely_cases.append({"id": item.premise_case.id, "title": item.premise_case.title})
    print(rely_cases)
    return rely_cases
