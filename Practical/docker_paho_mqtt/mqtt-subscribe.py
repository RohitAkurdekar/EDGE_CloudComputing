
import paho.mqtt.client as mqtt
from notification_handler import send_notification
from anamoly_handler import send_alert

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    try:
        print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
        client.subscribe("cdac/docker/testing")
    except Exception as e:
            print("Exception in Subscribe_block",e)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    try:
        print(msg.topic+" "+str(msg.payload))
        print("data received",msg.payload.decode())
        data_received = int(msg.payload.decode())
        print(type(data_received))
        if isinstance(data_received,int):
            if data_received > 10 and  data_received <= 20:
                send_notification("Inserting the data in the MYSQL table for Edge Analytics")
            if data_received < 0:
                data_formatting_for_anamoly(data_received)
            if data_received > 50:
                data_formatting_for_anamoly(data_received)
        else:
            print("Sending data to cloud")
    
    except Exception as e:
        print("Exception in on_message block",e)

def data_formatting_for_anamoly(data_received):
    username = "diot1"
    deviceid = "test_device1"
    sensor_name = "DHT11"
    sensor_value = data_received
    print("running in anamoly block")
    print("data in anamoly block",data_received)
    send_alert(username,deviceid,sensor_name,sensor_value)



try:
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("192.168.77.208", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
    client.loop_forever()
except Exception as e:
    print("Exception in main",e)




