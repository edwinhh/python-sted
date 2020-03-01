from django.test import TestCase

# Create your tests here.
# from celery_tasks.run.tasks import task_demo
#
#
# task_id = task_demo.delay([1,2,3],2)
# print(task_id)



from celery_tasks.demo.tasks import add
# 固定celery的调用方式
add.delay()

