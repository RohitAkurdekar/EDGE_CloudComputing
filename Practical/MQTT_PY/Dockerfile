# MQTT using python

FROM python:3.12-rc-buster

LABEL "developer"="RohitAkurdekar"

WORKDIR /app/mqttapp/

ADD . /app/mqttapp/

RUN pip install -r requirements.txt

CMD ["python","subscriber.py"]