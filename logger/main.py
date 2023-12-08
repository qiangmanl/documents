import logger 


x=11
@logger.prompt("warning")
def f(x):
    raise Exception("sdadsa")

f(x)

import asyncio 

@logger.aprompt("warning")
async def get(x):
    await asyncio.sleep(0)
    # 1/0
    return x

async def main(x=1):
    x = await get(x=x)
    print(x)
asyncio.get_event_loop().run_until_complete(main(x))