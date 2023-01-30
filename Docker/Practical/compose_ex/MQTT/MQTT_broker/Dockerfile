FROM ubuntu:20.04

LABEL "developer"="rohit akurdekar"

RUN apt update -y && apt install mosquitto -y

# RUN service mosquitto start

CMD ["/usr/sbin/mosquitto"]

EXPOSE 1883