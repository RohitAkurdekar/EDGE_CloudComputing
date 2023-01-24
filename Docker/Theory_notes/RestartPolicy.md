# Auto restart policy

    diot@diot:~/$ docker run --restart always alpine:diothello 
    Hello From the alpine developed by diot batch
    
    diot@diot:~/$ docker ps 
    CONTAINER ID   IMAGE              COMMAND                  CREATED          STATUS  PORTS     NAMES
    4043ab4de55e   alpine:diothello   "echo 'Hello From th…"   32 seconds ago   Restarting (0) 6 seconds ago             zealous_perlman
    
    diot@diot:~/$ docker ps 
    CONTAINER ID   IMAGE              COMMAND                  CREATED          STATUS  PORTS     NAMES
    4043ab4de55e   alpine:diothello   "echo 'Hello From th…"   35 seconds ago   Restarting (0) 8 seconds ago             zealous_perlman

    diot@diot:~/$ docker ps 
    CONTAINER ID   IMAGE              COMMAND                  CREATED          STATUS  PORTS     NAMES
    4043ab4de55e   alpine:diothello   "echo 'Hello From th…"   38 seconds ago   Restarting (0) 12 seconds ago             zealous_perlman

    diot@diot:~/$ docker ps 
    CONTAINER ID   IMAGE              COMMAND                  CREATED          STATUS  PORTS     NAMES
    4043ab4de55e   alpine:diothello   "echo 'Hello From th…"   40 seconds ago   Up Less than a second             zealous_perlman
    
    diot@diot:~/$ docker ps 
    CONTAINER ID   IMAGE              COMMAND                  CREATED          STATUS  PORTS     NAMES
    4043ab4de55e   alpine:diothello   "echo 'Hello From th…"   42 seconds ago   Restarting (0) 1 second ago             zealous_perlman
    
    diot@diot:~/$ docker ps 
    CONTAINER ID   IMAGE              COMMAND                  CREATED          STATUS  PORTS     NAMES
    4043ab4de55e   alpine:diothello   "echo 'Hello From th…"   44 seconds ago   Restarting (0) 4 seconds ago             zealous_perlman

-------------------------------------------------------------------------------------------------------

2023, Rohit Akurdekar