#!/usr/bin/python3

# import modules
import json
from time import sleep
import paho.mqtt.publish as publisher
import random

# CONSTANTS
TOPIC       = 'akurdekar/rohit'
BROKER_ADDR = "mqttbroker"
PORT        = 1883
KEEP_ALIVE  = 60

# variables
# Dummy device data
data = {
    "api_key" : "J76GYFXE11UWQ68N",     # API key 
    "field1"  : "Rohit Akurdekar",      # Patient name
    "field2"  : 80,                     # O2 saturation
    "field3"  : 75,                     # step count
    "field4"  : 8,                      # sleep hours

}


# Callback method for successful connection
def on_connect(client, userData, flags, responseCode):
    print("Connected to MQTT broker")
    publisher.subscribe(TOPIC)


# Defining callback methods in MQTT  Client
publisher.on_connect = on_connect

while True:
# Send single publish request to broker
    publisher.single(topic=TOPIC,
                    payload=json.dumps(data),
                    hostname=BROKER_ADDR,
                    port=PORT,
                    qos=2,
                    keepalive=KEEP_ALIVE)

    print("meassage: "+json.dumps(data))
    sleep(5)            # Wait for 5 seconds

    # Generate a random data using dummy device
    data = {
        "api_key"   : "J76GYFXE11UWQ68N",  
        "field1"    : "Rohit Akurdekar",   
        "field2"    : random.randint(1,31),
        "field3"    : random.randint(60,91),
        "field4"    : random.randint(450,601),
    }



""" 
#!/usr/bin/python3

# import paho.mqtt.client as mqtt
import paho.mqtt.publish as publisher

# CONSTANTS
TOPIC       = 'cdac/diot'
BROKER_ADDR = "mqttbroker"
PORT        = 6800
KEEP_ALIVE  = 60 

# Callback method for successful connection
def on_connect(client, userData, flags, responseCode):
    print("Connected to MQTT broker")
    publisher.subscribe(TOPIC)


# Defining callback methods in MQTT  Client
publisher.on_connect = on_connect
i =0
while True:
    i+=1
    data = "num: "+i
    # Send single publish request to broker
    publisher.single(topic=TOPIC,
                    payload=data,
                    hostname=BROKER_ADDR,
                    port=PORT,
                    qos=2,
                    keepalive=KEEP_ALIVE)

 """