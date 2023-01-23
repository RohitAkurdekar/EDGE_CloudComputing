# Docker hub


    $ docker tag local-image:tagname new-repo:tagname
    $ docker push new-repo:tagname    

-----------------------------------------------------------------------------------------------------

    REPOSITORY     TAG                 IMAGE ID       CREATED             SIZE
    ubuntu         mqttbrokerV0        1699986f2c92   About an hour ago   121MB

------------------------------------------------------------------------------------------------------

    diot@diot:~/$ docker tag ubuntu:mqttbrokerV0 rohitakurdekar/jan2023:mqttbroker
    
    diot@diot:~/$ docker push rohitakurdekar/jan2023:mqttbroker 
    The push refers to repository [docker.io/rohitakurdekar/jan2023]
    12c1f5c9c126: Pushed 
    e99341eebcd7: Pushed 
    8fad4f98204c: Pushed 
    b268153ce17f: Pushed 
    0f54518c0204: Pushed 
    0b1dee4127fc: Pushed 
    2bb16d894068: Pushed 
    0002c93bdb37: Mounted from library/ubuntu 
    mqttbroker: digest: sha256:866fade2e6e09ff48b80b0a87b8484ae1248beb44cb0bf7fbcabe8c049da2fbc size: 1990

-----------------------------------------------------------------

    diot@diot:~/$ docker pull bhupendrajmd/sept2022:mqttedgesubscriber
    
    mqttedgesubscriber: Pulling from bhupendrajmd/sept2022
    ac7f2e1c7586: Already exists 
    dbcdf7fce05b: Already exists 
    0ed0c2752d84: Already exists 
    bf01cd4ea334: Already exists 
    739282cf09da: Already exists 
    852c00e61b55: Already exists 
    d71f968eaab0: Already exists 
    cd17469670c9: Already exists 
    10f6cec937ad: Already exists 
    4ffc616e4bb1: Pull complete 
    0c9ee49e3f88: Pull complete 
    cc2f70300bf8: Pull complete 
    Digest: sha256:485a595da7547365bd218acac90b216e2825e5b9503a0b51a9f66f8232e7b77d
    Status: Downloaded newer image for bhupendrajmd/sept2022:mqttedgesubscriber
    docker.io/bhupendrajmd/sept2022:mqttedgesubscriber    