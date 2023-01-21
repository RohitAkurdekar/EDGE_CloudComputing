    diot@diot:~/Documents/Rohit/EDGE_and_CloudComputing/Practical/MQTT_PY$ sudo docker build -t mqttpysub:v0 .
    Sending build context to Docker daemon  6.144kB
    Step 1/6 : FROM python:3.12-rc-buster
    ---> c4c556d42210
    Step 2/6 : LABEL "developer"="RohitAkurdekar"
    ---> Using cache
    ---> bf60f53800f7
    Step 3/6 : WORKDIR /app/mqttapp/
    ---> Using cache
    ---> 2eabb75d729b
    Step 4/6 : ADD /app/mqttapp/ .
    ADD failed: file not found in build context or excluded by .dockerignore: stat app/mqttapp/: file does not exist
    diot@diot:~/Documents/Rohit/EDGE_and_CloudComputing/Practical/MQTT_PY$ sudo docker build -t mqttpysub:v0 .
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
    ---> eb2dd6899d7d
    Step 5/6 : RUN pip insta -r requirements.txt
    ---> Running in 2997a286a96d
    ERROR: unknown command "insta" - maybe you meant "install"
    The command '/bin/sh -c pip insta -r requirements.txt' returned a non-zero code: 1
    diot@diot:~/Documents/Rohit/EDGE_and_CloudComputing/Practical/MQTT_PY$ sudo docker images
    REPOSITORY     TAG                 IMAGE ID       CREATED          SIZE
    <none>         <none>              eb2dd6899d7d   21 seconds ago   910MB
    ubuntu         ping                2358e25b63fe   2 hours ago      121MB
    python         3.12-rc-buster      c4c556d42210   2 days ago       910MB
    pythondemo     v2                  4cb12ae2024c   2 days ago       50.1MB
    pythondemo     v1                  f400cc860070   2 days ago       50.1MB
    centos_image   v1                  e0e4dd5e9c37   2 days ago       231MB
    python         3.10.9-alpine3.17   c8b069641107   10 days ago      50.1MB
    ubuntu         latest              6b7dfa7e8fdb   6 weeks ago      77.8MB
    hello-world    latest              feb5d9fea6a5   16 months ago    13.3kB
    centos         7                   eeb6ee3f44bd   16 months ago    204MB
    centos         centos8             5d0da3dc9764   16 months ago    231MB
    centos         latest              5d0da3dc9764   16 months ago    231MB
    diot@diot:~/Documents/Rohit/EDGE_and_CloudComputing/Practical/MQTT_PY$ sudo docker build -t mqttpysub:v0 .
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
    diot@diot:~/Documents/Rohit/EDGE_and_CloudComputing/Practical/MQTT_PY$ sudo docker run -it --name my_mqtt_sub mqttsub:v0
    Unable to find image 'mqttsub:v0' locally
    docker: Error response from daemon: pull access denied for mqttsub, repository does not exist or may require 'docker login': denied: requested access to the resource is denied.
    See 'docker run --help'.
    diot@diot:~/Documents/Rohit/EDGE_and_CloudComputing/Practical/MQTT_PY$ sudo docker run -it --name my_mqtt_sub mqttpysub:v0
    Connected to MQTT broker
    Topic: cdac/diot Message: b'dbvsaf'
    Topic: cdac/diot Message: b'aefea'
    ^CTraceback (most recent call last):
    File "/app/mqttapp/subscriber.py", line 32, in <module>
        subscriber.loop_forever()
    File "/usr/local/lib/python3.12/site-packages/paho/mqtt/client.py", line 1756, in loop_forever
        rc = self._loop(timeout)
            ^^^^^^^^^^^^^^^^^^^
    File "/usr/local/lib/python3.12/site-packages/paho/mqtt/client.py", line 1150, in _loop
        socklist = select.select(rlist, wlist, [], timeout)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    KeyboardInterrupt
    diot@diot:~/Documents/Rohit/EDGE_and_CloudComputing/Practical/MQTT_PY$ 



--------------------------------------------------------------------------------------

    diot@diot:~/Documents/Rohit/EDGE_and_CloudComputing/Practical/MQTT_PY$ mosquitto_pub -t cdac/diot -h 192.168.77.205 -l
    dbvsaf
    aefea
    ^C