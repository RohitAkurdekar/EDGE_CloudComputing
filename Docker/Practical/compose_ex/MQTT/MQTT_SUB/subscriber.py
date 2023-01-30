#!/usr/bin/python3

import paho.mqtt.client as mqtt

# To subscribe
subscriber = mqtt.Client()

# CONSTANTS
TOPIC       = 'cdac/diot'
BROKER_ADDR = "mqttbroker"
PORT        = 6800
KEEP_ALIVE  = 60

# Callback method for successful connection
def on_connect(client, userData, flags, responseCode):
    print("Connected to MQTT broker")
    subscriber.subscribe(TOPIC)

# Callback method to print recieved message
def on_message(client,userData, msg):
    my_data= {  "data":msg.payload    }
    print('Topic: ' + msg.topic + ' Message: ' + str(msg.payload))


# Defining callback methods in MQTT  Client
subscriber.on_connect = on_connect
subscriber.on_message = on_message

# Send connection request to broker
subscriber.connect(host=BROKER_ADDR,port=PORT,keepalive=KEEP_ALIVE)

# To maintain the connection
subscriber.loop_forever()