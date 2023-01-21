FROM python:3.12-rc-buster

LABEL "Developer"="Vrush"

WORKDIR /app/mqttapp

ADD . /app/mqttapp/

RUN pip install -r requirements.txt

CMD [ "python","mqtt-subscribe.py" ]
