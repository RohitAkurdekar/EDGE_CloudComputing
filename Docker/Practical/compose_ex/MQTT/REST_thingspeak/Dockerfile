# Subscriber
FROM python:3.12-rc-buster

LABEL "developer"="RohitAkurdekar"

WORKDIR /app/mqttapp/

ADD . /app/mqttapp/

RUN pip install paho-mqtt

RUN pip install requests

# RUN pip install json

# CMD ["python3","REST_API.py"]