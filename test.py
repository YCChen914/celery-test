from tasks import add

# 透過 Celery 派送工作
result = add.delay(4, 4)

while(True):
    print(result.ready())
    if(result.ready()==True):
        print(result.get())
        break

# 釋放儲存空間 
#result.forget()
