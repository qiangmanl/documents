from sanic import request
from sanic.response import json
from server.sql import relay_ctrol
from server.config import devices


async def hello(request:request.Request):
    return json({'hello': 'world'})


async def listen_relay_task(request: request.Request, *args, **kwargs):
    # uri post some task
    if request.method == "POST":
        channel = request.json.get("channel", None)
        switch = request.json.get("switch", None)
        device = request.json.get("device", None)
        if channel and switch:
            if device in devices:
                #save to sqlrequest
                data = relay_ctrol.update_relay_task(device, channel, switch, act=1)
                if not data:
                    return json({})
                return json(data)
    elif request.method == "GET":
        device = request.args.get('device')
        task = relay_ctrol.get_relay_task(device)
        print(task)
        if not task:
            return json({})
        return json(task)

        # return json({"latest_switch": switch,
        #              "activate_channel":ch,
        #              "device":device})


async def relay_do_task(request: request.Request, *args, **kwargs):
    device = request.args.get('device')
    task = relay_ctrol.get_relay_task(device)
    if not task:
        return json({})
    else:
        if task["act"] == 1:
            channel = task["ch"]
            switch = task["switch"]
            result = relay_ctrol.update_relay_task(device, channel, switch, act=0)
            if result["act"] == 0:
                result["device"] = device
                return json(result)
        else:
            task["device"] = device
            task["done"] = 1
            return json(task)

all=[hello, listen_relay_task,relay_do_task]