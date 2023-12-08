from beatheart import Looper
from beatheart import HeartBeat
from beatheart import MuitiTask
from beatheart import SingleTask
import asyncio          

heartbeat = HeartBeat(project="a",version="0.0.1",_print_interval=60)

class Test:
    def __init__(self):
        self.x = 1
        
    async def add_x(self,**kwargs):
        self.x += 1
        await asyncio.sleep(0)
        print(self.x)
    
test = Test()
MuitiTask.activate(heartbeat)
MuitiTask.register(test.add_x,1)
SingleTask.call_later(test.add_x,1)


looper = Looper(heartbeat)
looper.start()
