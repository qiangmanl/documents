import  uasyncio as asyncio
from tasks import tasks
from const import SSID, WIFI_PSWD
from utils import  connect_wifi
async def main():
    await asyncio.gather(*tasks)
print(tasks)

if __name__ == "__main__":
    if connect_wifi(SSID, WIFI_PSWD): 
        asyncio.run(main())
        
