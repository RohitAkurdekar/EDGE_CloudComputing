    diot@diot:~/$ sudo docker build -t mqttpysub:v0 .

    Sending build context to Docker daemon  6.144kB
    Step 1/6 : FROM python:3.12-rc-buster
    ---> c4c556d42210
    Step 2/6 : LABEL "developer"="RohitAkurdekar"
    ---> Using cache
    ---> bf60f53800f7
    Step 3/6 : WORKDIR /app/mqttapp/
    ---> Using cache
    ---> 2eabb75d729b
    Step 4/6 : ADD . /app/mqttapp/
    ---> 1954ffc86c84
    Step 5/6 : RUN pip install -r requirements.txt
    ---> Running in 7164c2720a69
    Collecting paho-mqtt
    Downloading paho-mqtt-1.6.1.tar.gz (99 kB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 99.4/99.4 kB 835.3 kB/s eta 0:00:00
    Preparing metadata (setup.py): started
    Preparing metadata (setup.py): finished with status 'done'
    Building wheels for collected packages: paho-mqtt
    Building wheel for paho-mqtt (setup.py): started
    Building wheel for paho-mqtt (setup.py): finished with status 'done'
    Created wheel for paho-mqtt: filename=paho_mqtt-1.6.1-py3-none-any.whl size=62118 sha256=7959949f707cb67c4f3a5a8ee5d3ca5a6b54e1c3dd8aa8c833dbbb8f1d210df9
    Stored in directory: /root/.cache/pip/wheels/b4/90/46/b3f3bad11f16428d2b87bc9a8c7d5a9721948a02c3733383ea
    Successfully built paho-mqtt
    Installing collected packages: paho-mqtt
    Successfully installed paho-mqtt-1.6.1
    WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
    Removing intermediate container 7164c2720a69
    ---> f8ee93ca8094
    Step 6/6 : CMD ["python","subscriber.py"]
    ---> Running in 99bd61fbe7f0
    Removing intermediate container 99bd61fbe7f0
    ---> 1d8822c20dd2
    Successfully built 1d8822c20dd2
    Successfully tagged mqttpysub:v0

--------------------------------- SUBSCRIBER ----------------------------------------------------

    diot@diot:~/$ sudo docker run -it --name my_mqtt_sub mqttpysub:v0
    
    Connected to MQTT broker
    Topic: cdac/diot Message: b'dbvsaf'
    Topic: cdac/diot Message: b'aefea'
    

--------------------------------- PUBLISHER -----------------------------------------------------

    diot@diot:~/$ mosquitto_pub -t cdac/diot -h 192.168.77.205 -l
    dbvsaf
    aefea