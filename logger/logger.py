from loguru import logger


class Logger:
    def __init__(self, path,rotation ,encoding ,enqueue , compression,retention, logger=logger):
        self.logger = logger
        self.logger.add(path, rotation=rotation, encoding=encoding, enqueue=enqueue, \
            compression=compression, retention=retention
        )
        self.debug = self.logger.debug
        self.info = self.logger.info
        self.warning = self.logger.warning
        self.error = self.logger.error
        self.exception = self.logger.exception

logger    = Logger(
    path="inter.log",
    rotation="500MB",
    encoding="utf-8",
    enqueue=True,
    compression="zip",
    retention="10 days"
)
debug     = logger.debug
info      = logger.info
warning   = logger.warning
error     = logger.error
exception = logger.exception


def prompt(courier="error"):
    """
        Usage:
            @logger.prompt("error")
            def test(): 
                return 1/0

            if not test():
                exit()
            print("test:yes")
            #Out:
                2023-12-02 11:14:29,411-ERROR-division by zero
    """

    def decorator(func):   
        def wrapper(*args, **kw):
            try: 
                result = func(*args, **kw) 
            except Exception as e:
                match courier:
                    case "error":
                        error(e) 
                    case "warning":
                        warning(e)
                    case "exception":
                        exception(e)
                    case _:
                        exception(f'{courier} Not an available courier!') 
                result = None
            return result
        return wrapper 
    return decorator

def aprompt(courier="error"):   
    """
    Usage:
        import asyncio 
        @adoubt("exception")
        async def get():
            await asyncio.sleep(0)
            1/0
            return 1

        async def main():
            x = await get()
            print(x)
        asyncio.get_event_loop().run_until_complete(main())
        #2023-12-05 21:42:38.291 | ERROR    | __main__:wrapper:87 - division by zero
    Return 
        None
    """
    def decorator(func):     
        async def wrapper(*args, **kw):
            try: 
                result = await func(*args, **kw) 
            except Exception as e: 
                match courier:
                    case "error":
                        error(e) 
                    case "warning":
                        warning(e)
                    case "exception":
                        exception(e)
                    case _:
                        exception(f'{courier} Not an available courier!')                 
                result = None
            return result
        return wrapper 
    return decorator

# def adoubt(courier="error",prompt="",**kw):   
#     """
#     Usage:
#         import asyncio 
#         @adoubt("exception")
#         async def get():
#             await asyncio.sleep(0)
#             1/0
#             return 1

#         async def main():
#             x = await get()
#             print(x)
#         asyncio.get_event_loop().run_until_complete(main())
#         #2023-12-05 21:42:38.291 | ERROR    | __main__:wrapper:87 - division by zero
#     Return 
#         None
#     """
#     try:
#         assert courier in loggers,"%s Not an available courier!"%courier
#         is_error = False
#     except AssertionError as e:
#         loggers["error"](e) #+ 
#         is_error = True
#     def decorator(func):     
#         async def wrapper(*args, **kw):
#             try: 
#                 if is_error:
#                     return None
#                 else:
#                     result = await func(*args, **kw) 
#             except Exception as e: 
#                 if prompt:
#                     loggers[courier](prompt) 
#                 else:
#                     loggers[courier](e)                    
#                 result = None
#             return result
#         return wrapper 
#     return decorator





