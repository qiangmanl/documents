# tasks.py
import time
from config import app
l=[1,2,3,34,4,5,5,8,6]
@app.task
def sendmail(mail):
    print('sending mail to %s...' % mail['to'])
    time.sleep(2.0)
    print('mail sent.')
    return mail

@app.task
def add(x, y):
    return  f'{time.ctime()}'

@app.task
def get_time(a,**kwargs):
    return f'{time.ctime()}__{a}'

@app.task
def pop_l():
    return l.pop()

# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # Calls test('hello') every 10 seconds.
#     sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

#     # Calls test('hello') every 30 seconds.
#     # It uses the same signature of previous task, an explicit name is
#     # defined to avoid this task replacing the previous one defined.
#     sender.add_periodic_task(30.0, test.s('hello'), name='add every 30')

#     # Calls test('world') every 30 seconds
#     sender.add_periodic_task(30.0, test.s('world'), expires=10)
# @app.task
# def test(arg):
#     print(arg)

# from tasks import add
# async
# add.delay(1,23)
# add(1,23)
    
# 实现定时任务的另一种方式
# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # sender.add_periodic_task(间隔时间秒, 
#     # 任务名.s(参数), name='自定义任务名')
#     sender.add_periodic_task(3, get_time.s("ss"), 
#                              name='crontab_func1 every 10')


