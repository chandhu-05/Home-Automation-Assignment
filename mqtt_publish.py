import paho.mqtt.client as mqtt
import time
import random

student_name = "R. Chandra Sekhar Reddy"
unique_id = "42110213"

base_topic = "home/chandrasekhar-2025/sensor"

client = mqtt.Client()
client.username_pw_set("mqttuser", "mqttpass123")
client.connect("192.168.1.16", 1883, 60)

while True:
    temperature = random.randint(20, 35)
    humidity = random.randint(40, 80)
    vibration = random.randint(0, 5)

    client.publish(base_topic + "/temp", temperature)
    client.publish(base_topic + "/humidity", humidity)
    client.publish(base_topic + "/vibration", vibration)

    print(f"Published → Temp:{temperature}  Hum:{humidity}  Vib:{vibration}")
    time.sleep(3)
