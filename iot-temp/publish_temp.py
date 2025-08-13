import random, sys, time
import paho.mqtt.client as mqtt

broker = sys.argv[1]
topic = sys.argv[2]

value = round(random.uniform(20.0, 28.0), 2)
client = mqtt.Client()
client.connect(broker, 1883, 60)
payload = {"temp_c": value, "ts": int(time.time())}
client.publish(topic, str(payload), qos=0, retain=False)
client.disconnect()
