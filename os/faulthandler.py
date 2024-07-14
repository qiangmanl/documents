import sys
import signal
import faulthandler
import io
import time
import pdb
"""
发送  kill -SIGUSR1 $程序PID 可以观察死锁位置，注册 SIGUSR1 信号处理函数 之后可以发送kill可以调用一次
"""
def _register_fault_handler():
    # 一些库会修改 stderr，我们需要实际的文件描述符
    if isinstance(sys.__stderr__, io.TextIOWrapper):
        faulthandler.register(signal.SIGUSR1, file=sys.__stderr__)

_register_fault_handler()

def sigusr1_handler(signum, frame):
    print("SIGUSR1 received, entering pdb...")
    

# 注册 SIGUSR1 信号处理函数
signal.signal(signal.SIGUSR1, sigusr1_handler)

def infinite_loop():
    x = 1
    while True:
        x += 1
        time.sleep(1)
        print(f"运行中...{x}")

if __name__ == "__main__":
    infinite_loop()


