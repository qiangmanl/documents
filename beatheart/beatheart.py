import asyncio
import random
import string
import signal
import inspect

def get_task_id(length=18):
    char = string.ascii_letters + string.digits
    return ''.join(random.choice(char) for _ in range(length))


__all__ = ("heartbeat","looper","MuitiTask","SingleTask")


class HeartBeat(object):
    """ 心跳
    """

    def __init__(self,project, version, _print_interval,logger=print):
        self.__project = project
        self.__version = version
        self.logger=logger
        self._count = 0  # 心跳次数
        self._interval = 0.005  # 服务心跳执行时间间隔(秒)
        self._print_interval = _print_interval  # 心跳打印时间间隔(秒)，0为不打印
        self._tasks = {}  # 跟随心跳执行的回调任务列表，由 self.register 注册 {task_id: {...}}

    def get_version(self):
        return self.__version
    
    def get_project(self):
        return self.__project

    @property
    def count(self):
        return self._count

    def ticker(self):
        """ 启动心跳， 每interval间隔执行一次
        """
        self._count += 1

        # 打印心跳次数
        if self._print_interval > 0:
            if self._count % int(self._print_interval* 200) == 0:
                msg = f'MSG:::HeartBeat.ticker:::do server [{self.__project}:{self.__version}] heartbeat, count:{int(self._count / 200)}'
                self.logger(msg)

        # 设置下一次心跳回调
        asyncio.get_event_loop().call_later(self._interval, self.ticker)

        # 执行任务回调
        for task_id, task in self._tasks.items():
            interval = task["interval"]
            if self._count % int(interval*200) != 0:
                continue
            func = task["func"]
            args = task["args"]
            kwargs = task["kwargs"]
            kwargs["task_id"] = task_id
            kwargs["heart_beat_count"] = self._count
            asyncio.get_event_loop().create_task(func(*args, **kwargs))

    def register(self, func, interval=1, *args, **kwargs):
        """ 注册一个任务，在每次心跳的时候执行调用
        @param func 心跳的时候执行的函数
        @param interval 执行回调的时间间隔(秒)
        @return task_id 任务id
        """
        t = {
            "func": func,
            "interval": interval,
            "args": args,
            "kwargs": kwargs
        }
        task_id = get_task_id()
        self._tasks[task_id] = t
        return task_id

    def unregister(self, task_id):
        """ 注销一个任务
        @param task_id 任务id
        """
        if task_id in self._tasks:
            self._tasks.pop(task_id)



class Looper:
    """ Asynchronous driven quantitative trading framework.
    """

    def __init__(self, heartbeat, logger=print):
        self._heartbeat = heartbeat
        self.loop = None
        self.__project = heartbeat.get_project()
        self.__version = heartbeat.get_version()
        self.logger = logger
        self.logger(f'MSG:::Looper:::[{self.__project}:{self.__version}] initiating...')
        self._get_event_loop()
        self._beat_heart()

    def start(self):
        """Start the event loop."""
        def keyboard_interrupt(s, f):
            print("KeyboardInterrupt (ID: {}) has been caught. Cleaning up...".format(s))
            self.loop.stop()
        signal.signal(signal.SIGINT, keyboard_interrupt)

        self.logger(f'MSG:::Looper:::Start in \"[{self.__project}:{self.__version}]\" io loop...')
        self.loop.run_forever()

    def stop(self):
        """Stop the event loop."""
        self.logger(f'MSG:::Looper:::Stop in \"[{self.__project}:{self.__version}]\" io loop...')
        self.loop.stop()

    def _get_event_loop(self):
        """ Get a main io loop. """
        if not self.loop:
            self.loop = asyncio.get_event_loop()
            #self.loop.set_debug(True)
        return self.loop

    def _beat_heart(self):
        """Start server heartbeat."""
        self.loop.call_later(0.5, self._heartbeat.ticker)

class MuitiTask(object):
    """ Loop run task.
    """
    @classmethod
    def activate(cls, heartbeat):
        cls.heartbeat = heartbeat

    @classmethod
    def register(cls, func, interval=1, *args, **kwargs):
        """ Register a loop run.

        Args:
            func: Asynchronous callback function.
            interval: execute interval time(seconds), default is 1s.

        Returns:
            task_id: Task id.
        """
        task_id = cls.heartbeat.register(func, interval, *args, **kwargs)
        return task_id

    @classmethod
    def unregister(cls, heartbeat ,task_id):
        """ Unregister a loop run task.

        Args:
            task_id: Task id.
        """
        heartbeat.unregister(task_id)


class SingleTask:
    """ Single run task.
    """

    @classmethod
    def run(cls, func, *args, **kwargs):
        """ Create a coroutine and execute immediately.

        Args:
            func: Asynchronous callback function.
        """
        asyncio.get_event_loop().create_task(func(*args, **kwargs))

    @classmethod
    def call_later(cls, func, delay=0, *args, **kwargs):
        """ Create a coroutine and delay execute, delay time is seconds, default delay time is 0s.

        Args:
            func: Asynchronous callback function.
            delay: Delay time is seconds, default delay time is 0, you can assign a float e.g. 0.5, 2.3, 5.1 ...
        """
        # import pdb 
        # pdb.set_trace()
        if not inspect.iscoroutinefunction(func):
            asyncio.get_event_loop().call_later(delay, func, *args)
        else:
            def foo(f, *args, **kwargs):
                asyncio.get_event_loop().create_task(f(*args, **kwargs))
            asyncio.get_event_loop().call_later(delay, foo, func, *args)


