```bash
cat >/tmp/broke.py<<EOF

from sanic import Sanic
from sanic import response
#pip install paho-mqtt
from paho.mqtt import client as mqtt

app = Sanic(__name__)
mqtt_client = mqtt.Client()

# MQTT连接回调函数
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
    else:
        print("Connection failed")

# MQTT消息接收回调函数
def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()}")

# Sanic路由处理函数，用于发布MQTT消息
@app.route("/publish", methods=["POST"])
async def publish(request):
    message = request.json.get("message")
    mqtt_client.publish("my/topic", message)
    return response.json({"status": f"Message {message} published"})

# Sanic应用程序启动时连接到MQTT代理
@app.listener("before_server_start")
async def setup_mqtt(app, loop):
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.connect("192.168.10.254", port=1883)
    mqtt_client.loop_start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8200)



#curl -X POST -H "Content-Type: application/json" -d '{"message": "Hello, MQTT!"}' http://localhost:8200/publish
EOF
python /tmp/broke.py
```