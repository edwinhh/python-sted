from celery_tasks.main import app
from django.conf import settings
from django.core.cache import cache
import json
#read cache user id
# def read_from_cache(user_name):
#     key =user_name
#     print ("key:",key)
#     value = cache.get(key)
#     if value == None:
#         data = "NOne,no data"
#     else:
#         data = json.loads(value)
#     return data
#write cache user id
# def write_to_cache(user_name):
#     key = 'user_id_of_'+user_name
#     cache.set(key, json.dumps(user_name))
# broker_url = "redis://@127.0.0.1:6379/4"
# result_backend ="redis://@127.0.0.1:6379/4"
#
# app = Celery('tasks',broker=broker_url,backend=result_backend)  # 配置好celery的backend和broker

@app.task(name="task_test")  # 普通函数装饰为 celery task
def add():
    print ("ok")

