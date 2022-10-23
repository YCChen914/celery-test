from celery import Celery


# 建立 Celery Application
app = Celery('tasks', backend='rpc://', broker='redis://localhost/')

# 定義工作函數
@app.task
def add(x, y):
    for i in range(500):
        z=0
    return x + y