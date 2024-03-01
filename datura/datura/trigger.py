import asyncio
import signal
import time
from datura import logger


class Engine:
    def __init__(self,project_name, interval, print_interval)->None:
        self.loop = asyncio.get_event_loop()
        self.project_name = project_name
        logger.info(f'{self.project_name} MSG:::{self.__class__.__name__}:::[project:{self.project_name}] initiating...')
        self.is_starting = False
        self._count = 0  # 心跳次数
        self._interval = round(interval,7) or 1/10 ** 7
        self._print_interval = int(print_interval) if print_interval > 0 else 60
        self._task = None
        self._print_count = 0
        self._print_done = False

    def register(self, func, *args, **kwargs)->str:
        """ 注册一个任务，在每次心跳的时候执行调用
        @param func 心跳的时候执行的函数,时间间隔self._interval
        """
        task = {
            "func": func,
            "args": args,
            "kwargs": kwargs
        }
        self._task = task
        return task
    
    def unregister(self):
        del self._task
        self._task = None

    def ticker(self):
        """ 
        """
        self._count += 1

        # 下一次心跳间隔
        self.loop.call_later(self._interval, self.ticker)
        func = self._task["func"]
        args = self._task["args"]
        kwargs = self._task["kwargs"]
        self.loop.create_task(func(*args, **kwargs))
        if (int(time.time()) % self._print_interval) == 0:
            if self._print_done == True:
                return
            else:
                self._print_count += 1
                msg = f'{self.__class__.__name__} MSG:::{self.__class__.__name__}.ticker:::doing task:{func.__name__}, count:{self._print_count}'
                logger.info(msg)
                self._print_done = True
        else:
            if self._print_done == True:
                self._print_done = False

    def _ignite(self):
        """Start server heartbeat."""
        self.loop.call_later(0.5, self.ticker)
        logger.info("all heartbeat ticked")
        self.is_starting = True

    def run_forever(self):
        """Start the event loop."""
        self._ignite()
        def keyboard_interrupt(s, f):
            logger.info(f"KeyboardInterrupt (ID: {s}) has been caught. engine stop...")
            self.loop.stop()
        signal.signal(signal.SIGINT, keyboard_interrupt)
        logger.info(f'{self.project_name} MSG:::{self.__class__.__name__}:::Start \"[project:{self.project_name}]\" io loop...')
        self.loop.run_forever()

    def stop(self):
        """Stop the event loop."""
        logger.info(f'{self.project_name} MSG:::{self.__class__.__name__}:::Stop \"[project:{self.project_name}]\" io loop...')
        self.loop.stop()

# class Trigger:
#     def __init__(self) -> None:
#         self.loop = asyncio.get_event_loop()
#         logger.info(f'{self.project_name} MSG:::Trigger:::[project:{local.project_name}] initiating...')
#         self.is_starting = False
#         import pdb
#         pdb.set_trace()