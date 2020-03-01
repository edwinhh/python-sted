# 在celery中使用logger
from celery.utils.log import get_task_logger
from utils.send_message import send_email

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


# 用例运行
@app.task(name='run_case')
def run_case(case_id, user_id):
    task_id = run_case.request.id
    print("task_id",task_id)
    print(case_id)
    print(user_id)

# 集合运行
@app.task(name='run_collection')
def run_collection(collect_id,user_id):
    task_id = run_collection.request.id
    print("task_id",task_id)
    print(collect_id)
    print(user_id)

def run(case_id):
    '''单个用例原型'''
    pass


@app.task(name="task_test")  # 普通函数装饰为 celery task
def add():
    print ("ok")
#  获取依赖用例
# A B C
# A依赖于B B依赖于C  --- 》 真实情况 不清楚业务会配多少层依赖关系。
#
# 我们运行A。。。？？？？


