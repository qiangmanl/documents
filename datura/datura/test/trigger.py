import asyncio
from datura.trigger import Engine
from datura import local
import time

class A:
    def __init__(self):
        pass

    async def task(self):
        await asyncio.sleep(0)
        print(time.time())


a = A()
e = Engine(local.project_name,1,3)
e.register(a.task)
e.run_forever()