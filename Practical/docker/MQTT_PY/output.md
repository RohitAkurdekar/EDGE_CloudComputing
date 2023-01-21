
--------------------- BUILD DOCKER IMAGE -----------------------------------

    diot@diot:~/$ docker build -t mqttpysub:v2 .

    Sending build context to Docker daemon  13.82kB
    Step 1/6 : FROM python:3.12-rc-buster
    ---> c4c556d42210
    Step 2/6 : LABEL "developer"="RohitAkurdekar"
    ---> Using cache
    ---> bf60f53800f7
    Step 3/6 : WORKDIR /app/mqttapp/
    ---> Using cache
    ---> 2eabb75d729b
    Step 4/6 : ADD . /app/mqttapp/
    ---> ec376a9063de
    Step 5/6 : RUN pip install -r requirements.txt
    ---> Running in c26ea2b1faca
    Collecting paho-mqtt
    Downloading paho-mqtt-1.6.1.tar.gz (99 kB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 99.4/99.4 kB 766.1 kB/s eta 0:00:00
    Preparing metadata (setup.py): started
    Preparing metadata (setup.py): finished with status 'done'
    Collecting pymongo
    Downloading pymongo-4.3.3.tar.gz (814 kB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 814.2/814.2 kB 4.3 MB/s eta 0:00:00
    Preparing metadata (setup.py): started
    Preparing metadata (setup.py): finished with status 'done'
    Collecting dnspython<3.0.0,>=1.16.0
    Downloading dnspython-2.3.0-py3-none-any.whl (283 kB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 283.7/283.7 kB 7.0 MB/s eta 0:00:00
    Building wheels for collected packages: paho-mqtt, pymongo
    Building wheel for paho-mqtt (setup.py): started
    Building wheel for paho-mqtt (setup.py): finished with status 'done'
    Created wheel for paho-mqtt: filename=paho_mqtt-1.6.1-py3-none-any.whl size=62118 sha256=7d6203a07ec1b91ddd594b908e1c053574ceb84214cdd248f3ec2466ed7561b7
    Stored in directory: /root/.cache/pip/wheels/b4/90/46/b3f3bad11f16428d2b87bc9a8c7d5a9721948a02c3733383ea
    Building wheel for pymongo (setup.py): started
    Building wheel for pymongo (setup.py): finished with status 'done'
    Created wheel for pymongo: filename=pymongo-4.3.3-cp312-cp312-linux_x86_64.whl size=514576 sha256=3b63ff99304ff38aa28d4de64465bd911eac3270901a55dd776976bbc18d4574
    Stored in directory: /root/.cache/pip/wheels/d4/20/4d/e0a01c69b694f6aa6486a327b4732c472abd11b03f4e4a01b8
    Successfully built paho-mqtt pymongo
    Installing collected packages: paho-mqtt, dnspython, pymongo
    Successfully installed dnspython-2.3.0 paho-mqtt-1.6.1 pymongo-4.3.3
    WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
    Removing intermediate container c26ea2b1faca
    ---> 737586452d3a
    Step 6/6 : CMD ["python","subscriber.py"]
    ---> Running in ba73da4d9add
    Removing intermediate container ba73da4d9add
    ---> 5477fddfc047
    Successfully built 5477fddfc047
    Successfully tagged mqttpysub:v2

--------------------- CREATE CONTAINER USING IMAGE -----------------------------------

    diot@diot:~/$ docker run -it --name mqtt_demo_v1 mqttpysub:v2

    Connected successfully!!!
    Connected to MQTT broker
    Data inserted successfully...!!!
    Topic: cdac/diot Message: b'message'
    Data inserted successfully...!!!
    Topic: cdac/diot Message: b'{"sensor_name":"DHT11","sensor_value":15}'

--------------------- PUBLISH DATA OVER MQTT -----------------------------------


    mosquitto_pub -h 192.168.77.205 -t cdac/diot -l
    message
    {"sensor_name":"DHT11","sensor_value":15}


--------------------- READ COLLECTIONS -----------------------------------------

    diot@diot:~/$ python3 readCollectionMongo.py 

    Connected successfully!!!
    {'_id': ObjectId('63cb7ad89115f80fc870be08'), 'data': b'This is python publisher'}
    {'_id': ObjectId('63cb7fc0ca5bdd9514b107b3'), 'data': b'message'}
    {'_id': ObjectId('63cb7feeca5bdd9514b107b4'), 'data': b'{"sensor_name":"DHT11","sensor_value":15}'}
