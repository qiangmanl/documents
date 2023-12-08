#### 
```bash
celery -A tasks worker --loglevel=info
#如果需要定时任务
celery -A tasks beat
#
```
```python
from tasks import sendmail
x = sendmail.delay(dict(to='celery@python.org'));print(x.successful())
#False
print(x.successful())
#True
from tasks import add
result = add.delay(4,4)

result.get()


for i in range(10):
    result = add.delay(i,i)
    print(result.get())
```


#### product and comsume
```python

#device1 
from tasks import pop_l
result = pop_l.delay()



#device2
from tasks import pop_l
result = pop_l.delay()

```