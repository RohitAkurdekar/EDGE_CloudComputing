
    docker compose up 
    clear
    docker rm mqc_broker &&
    docker rm mqc_pub &&
    docker rm mqc_sub &&
    docker rm mqc_rest &&

    docker rmi mqtt-mqttbroker:latest &&
    docker rmi mqtt-mqttsub:latest &&
    docker rmi mqtt-mqttpub:latest &&
    docker rmi mqtt-mqttrest:latest &&
    clear


    mqc_pub     | meassage: {"temperature": 11, "Humidity": 62, "pressure": 551, "location": "DIoT classrooom"}


    mqc_sub     | Topic: akurdekar/rohit Message: b'{"temperature": 15, "Humidity": 66, "pressure": 504, "location": "DIoT classrooom"}'

    mqc_broker  | 1675180476: New connection from 172.22.0.4 on port 1883.
    mqc_broker  | 1675180476: New client connected from 172.22.0.4 as auto-1A446796-2C81-FEEA-4559-927139B711D7 (p2, c1, k60).
    mqc_broker  | 1675180476: Client auto-1A446796-2C81-FEEA-4559-927139B711D7 disconnected.