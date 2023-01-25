# Subscriber
FROM python:3.12-rc-buster

LABEL "developer"="RohitAkurdekar"

WORKDIR /app/mqttapp/

ADD . /app/mqttapp/

RUN pip install paho-mqtt

CMD ["python","subscriber.py"]