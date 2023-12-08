import uasyncio  as asyncio
from protocal import AsyncWebsocketClient
from const import WS_SERVER, WEBSOCKET_DELAY
ws = AsyncWebsocketClient(WEBSOCKET_DELAY)
lock = asyncio.Lock()
data_from_ws = []
async def read_loop():
    global lock
    global data_from_ws
    
    while True:
        try:
            print("Handshaking...")
            # connect to test socket server with random client number
            if not await ws.handshake(uri = WS_SERVER):
                raise Exception('Handshake error.')
            print("...handshaked.")

            mes_count = 0
            while await ws.open():
                print(mes_count)
                # print("Data: " + str(data) + "; " + str(mes_count))
                # close socket for every 10 messages (even ping/pong)
                if mes_count == 10:
                    await ws.close()
                    print("ws is open: " + str(await ws.open()))
                    await asyncio.sleep(1)
                data = await ws.recv()
                print(data)
                await ws.send("daddadd")

                if data is not None:
                    await lock.acquire()
                    lock.release()

                await asyncio.sleep(1)
                mes_count += 1
        except Exception as ex:
            print(" A exception: {}".format(ex))
            await asyncio.sleep(1)


async def send_data():
    # Main "work" cycle. It should be awaitable as possible.
    
    send_counter = 0
    while True:
        send_counter = send_counter + 1
        if ws is not None:
            # delay to send data. 5 min, 5 * 60 * 1000 ms / 500 ms , 600
            if send_counter > 600: 
                if await ws.open(): 
                    #await ws.send("daddd")
                    #print('Data pushed!')
                    send_counter = 0

            # lock data archive and process in data
            await lock.acquire()
            await ws.send("daddadd")
            lock.release()

        await asyncio.sleep_ms(500)
# --------------------------------------------------   
    
tasks = []
tasks.append(read_loop())
#tasks.append(send_data())
__all__ = tasks
# ------------------------------------------------------