from celery_tasks.run.test import add

def notity(a, b):
    # result = a + b
    result = add.delay(a, b)
    return result

if __name__ == '__main__':
    result = notity(3, 5)
    print(result)