#!/usr/bin/python3

# import paho.mqtt.client as mqtt
import paho.mqtt.publish as publisher

# CONSTANTS
TOPIC       = 'cdac/diot'
BROKER_ADDR = "192.168.77.205"
PORT        = 1883
KEEP_ALIVE  = 60 

# Callback method for successful connection
def on_connect(client, userData, flags, responseCode):
    print("Connected to MQTT broker")
    publisher.subscribe(TOPIC)


# Defining callback methods in MQTT  Client
publisher.on_connect = on_connect


# Send single publish request to broker
publisher.single(topic=TOPIC,
                 payload="This is python publisher",
                 hostname=BROKER_ADDR,
                 port=PORT,
                 qos=2,
                 keepalive=KEEP_ALIVE)