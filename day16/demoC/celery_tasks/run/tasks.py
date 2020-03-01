from celery_tasks.main import app

@app.task
def demo_test():
    print(1111)