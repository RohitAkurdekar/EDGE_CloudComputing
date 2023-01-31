
    docker compose up 
    clear
    docker rm mqc_broker &&
    docker rm mqc_pub &&
    docker rm mqc_sub &&

    docker rmi mqtt-mqttbroker:latest &&
    docker rmi mqtt-mqttsub:latest &&
    docker rmi mqtt-mqttpub:latest