```python
import asyncio
from sanic import Sanic
from sanic.response import file, json

app = Sanic(__name__)

@app.websocket("/feed")
async def foo3(request, ws):
    while True:
    	await asyncio.sleep(1)
    	data = "hello!"
    	print("Sending: " + data)
    	await ws.send(data)
    	data = await ws.recv()
    	print("Received: " + data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1985, debug=True)
```
