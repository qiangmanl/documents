# coding: utf-8
from celery import Celery
from celery.schedules import crontab
from datetime import timedelta
celery_broker = 'amqp://guest@127.0.0.1//'
# celery_backend = 'amqp://guest@127.0.0.1//'

# Add tasks here
app = Celery('tasks' , broker='amqp://guest@localhost//')

app.conf.update(
    ACKS_LATE=True,  # 允许重试
    ACCEPT_CONTENT=['pickle', 'json'],
    TASK_SERIALIZER='json',
    RESULT_SERIALIZER='json',
    # 设置并发worker数量
    WORKER_CONCURRENCY=4, 
    # 每个worker最多执行500个任务被销毁，可以防止内存泄漏
    MAX_TASKS_PER_CHILD=500, 
    broker_heartbeat=0,  # 心跳
    TASK_TIME_LIMIT=12 * 30,  # 超时时间
    broker_connection_retry_on_startup=True,
    CELERY_ENABLE_UTC=True,
    TIMEZONE='Asia/Shanghai'
    
)


# 任务的定时配置


# # from celery.schedules import crontab
app.conf.beat_schedule = {
    'pop_l': {
        'task': 'tasks.pop_l',
        'schedule':   crontab(minute='*/1'),
     
    },
    'add': {
        'task': 'tasks.add',
        #'schedule':   crontab(minute='*/1'),
        'schedule': timedelta(seconds=3),
        # 每周一早八点

        # 'schedule': crontab(hour=8, day_of_week=1), 
        'args': (12,14),
    }
    
}
