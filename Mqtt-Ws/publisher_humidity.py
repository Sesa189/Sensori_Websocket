import time
import random
import json
import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
TOPIC = "cesare/sensor/humidty"

client = mqtt.Client()
client.connect(BROKER, 1883)

print("Sensore simulato avviato")

while True:
    value = round(random.uniform(97, 100), 2)

    payload = {
        "sensor": "temperature",
        "value": value,
        "unit": "%"
    }

    client.publish(TOPIC, json.dumps(payload))
    print("Pubblicato:", payload)

    time.sleep(1)
