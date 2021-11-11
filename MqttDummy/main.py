import os
import time

import paho.mqtt.client as mqtt

CLIENT_ID = os.environ.get('CLIENT_ID') or "TEST_ID"
PUB_TOPIC = os.environ.get('PUB_TOPIC') or "TEST_PUB"
print(f"PUB_TOPIC set to {PUB_TOPIC}")
SUB_TOPIC = os.environ.get('SUB_TOPIC') or "TEST_SUB"


def on_message(client, userdata, message):
    print(f"[{message.topic}] message received: ", str(message.payload.decode("utf-8")))


client = mqtt.Client(CLIENT_ID, transport='websockets')
client.on_message = on_message

client.connect('mqtt_broker', port=9001)

print(f"Subscribing to {SUB_TOPIC}")
client.subscribe(SUB_TOPIC)

client.loop_start()

while True:
    client.publish(PUB_TOPIC, f"Hello from {CLIENT_ID}")
    time.sleep(1)