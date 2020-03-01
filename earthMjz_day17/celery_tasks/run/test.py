from celery import Celery
import time


app = Celery('sksystem')
app.config_from_object('celery_tasks.config')

@app.task
def add(a, b):
    count = a + b
    print('任务函数正在执行....')
    time.sleep(5)
    return count
