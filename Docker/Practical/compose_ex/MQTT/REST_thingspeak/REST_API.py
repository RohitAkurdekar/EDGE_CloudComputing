#!/usr/bin/python3

# Program to perform simple GET request to HTTP server
import requests
import json

import paho.mqtt.client as mqtt


HOST = "https://api.thingspeak.com/update.json"

REQUEST_BODY = {
    "api_key"   : "J76GYFXE11UWQ68N",    # API key 
    "field1"    : "Rohit Akurdekar",      # Patient name
    "field2"    : 80,                     # O2 saturation
    "field3"    : 75,                     # step count
    "field4"    : 8,                      # sleep hours

}
# -----------------------------------------------------------
# To subscribe
subscriber = mqtt.Client()

# CONSTANTS
TOPIC       = 'akurdekar/rohit'
BROKER_ADDR = "mqttbroker"
PORT        = 1883
KEEP_ALIVE  = 60

def rest_post(data):

    RxdData = json.loads(data)

    print(RxdData)

    REQUEST_BODY["api_key"] = RxdData["api_key"]
    REQUEST_BODY["field1"]  = RxdData["field1"]
    REQUEST_BODY["field2"]  = RxdData["field2"]
    REQUEST_BODY["field3"]  = RxdData["field3"]
    REQUEST_BODY["field4"]  = RxdData["field4"]

    # REQUEST_BODY = msg.payload  
    response = requests.post(HOST , REQUEST_BODY)

    print(response.json())



# Callback method for successful connection
def on_connect(client, userData, flags, responseCode):
    print("Connected to MQTT broker")
    subscriber.subscribe(TOPIC)

# Callback method to print recieved message
def on_message(client,userData, msg):
    # my_data= {  "data":msg.payload    }
    # print('Topic: ' + msg.topic + ' Message: ' + str(msg.payload))

    print(str(msg.payload))
    rest_post(msg.payload)


# Defining callback methods in MQTT  Client
subscriber.on_connect = on_connect
subscriber.on_message = on_message

# Send connection request to broker
subscriber.connect(host=BROKER_ADDR,port=PORT,keepalive=KEEP_ALIVE)

# To maintain the connection
subscriber.loop_forever()

# --------------------------------------------------------