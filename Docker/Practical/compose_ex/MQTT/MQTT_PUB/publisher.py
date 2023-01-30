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
    # Send single publish request to broker
    publisher.single(topic=TOPIC,
                    payload=i,
                    hostname=BROKER_ADDR,
                    port=PORT,
                    qos=2,
                    keepalive=KEEP_ALIVE)