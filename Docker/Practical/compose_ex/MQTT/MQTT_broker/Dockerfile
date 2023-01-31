FROM ubuntu:20.04

LABEL "developer"="rohit akurdekar"

RUN apt update -y && apt install mosquitto -y

# RUN service mosquitto start

# RUN service mosquitto restart
# CMD ["service","mosquitto","status"]
CMD ["/usr/sbin/mosquitto"]

EXPOSE 1883