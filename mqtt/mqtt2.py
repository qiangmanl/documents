import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")
    client.subscribe("my/topic")

def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()}")

# def on_publish(client, userdata, mid):
#     print("Message published")
#     client.subscribe("my/topic")  # 在发布后订阅相同的主题

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
# client.on_publish = on_publish

client.connect("192.168.99.214", port=1883)
client.loop_start()

while True:
    time.sleep(10)
    client.publish("my/topic", "Hello, topic2!")
    pass

