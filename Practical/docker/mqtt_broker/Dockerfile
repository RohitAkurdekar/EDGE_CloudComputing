# MQTT broker image

FROM ubuntu:20.04
LABEL developer="rohitakurdekar"
WORKDIR /myapp/mqttbroker
ADD . /myapp/mqttbroker/

RUN apt update -y

RUN apt install mosquitto -y

RUN cp /myapp/mqttbroker/port.conf /etc/mosquitto/conf.d/

RUN service mosquitto restart