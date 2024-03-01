from beatheart import looper, MuitiTask, SingleTask

import asyncio          


class Test:
    def __init__(self):
        self.x = 1
        
    async def add_x(self,**kwargs):
        self.x += 1
        await asyncio.sleep(0)
        print(self.x)
    
test = Test()

MuitiTask.register(test.add_x,1)
SingleTask.call_later(test.add_x,1)



looper.start()
