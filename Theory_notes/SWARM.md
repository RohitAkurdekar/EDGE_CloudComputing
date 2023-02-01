# Docker SWARM 


Manager:-

    $ docker swarm init --advertise-addr <manager_IP>
    Swarm initialized: current node (p5pqeh7zpbeyaz5cj8ts0kt3x) is now a manager.

To add a worker to this swarm, run the following command:

    docker swarm join --token SWMTKN-1-5otkyji7evlf280bbadl4nxco9docrlwku13fx4gxp9zevwhxa-4ne97xhsrhhnglk8716e6gl6c <manager_IP>:2377

To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.

---------------------------------------------------------------------------------------------------

    diot@diot:~/$ docker node ls
    ID                            HOSTNAME      STATUS    AVAILABILITY   MANAGER STATUS   ENGINE VERSION
    p5pqeh7zpbeyaz5cj8ts0kt3x *   diot          Ready     Active         Leader           20.10.23
    dpy7fj373s98yegdqbuq87l4o     diot-05       Ready     Active                          20.10.23
    rzdmwn8vdrr40hkh2md1k9t1s     diot-06       Ready     Active                          20.10.23

-------------------------------------------------------------------------------------------------------

    diot@diot:~$ docker swarm leave
    Node left the swarm.

    diot@diot:~$ docker swarm join --token SWMTKN-1-2uhtc1gysm6bik8dciwvs7zmh6p70f41b603ek9pvngy82dffa-d2o9o8kolhw5foet4mdtrexkq 192.168.77.236:2377
    This node joined a swarm as a manager.

    diot@diot:~$ docker node ls
    ID                            HOSTNAME    STATUS    AVAILABILITY   MANAGER STATUS   ENGINE VERSION
    m77esfb3sm7deh0hru8fae6ke *   diot        Ready     Active         Reachable        20.10.23
    rfxv2veuqcwoh9ou6yqam2clr     diot        Down      Active                          20.10.23
    4pmc4b04xifge30elwp6hyvdu     diot        Ready     Active         Leader           20.10.23
    qpfy8v9pa1cug1nr9w0ph0hx4     diot        Ready     Active                          20.10.23
    xfqavu8x2vh17q19tjvb1c2b0     localhost   Ready     Active                          20.10.23
    diot@diot:~$ 

--------------------------------------------------------------------------------------------------------

    diot@diot:~$ docker swarm init --force-new-cluster
    Swarm initialized: current node (m77esfb3sm7deh0hru8fae6ke) is now a manager.

--------------------------------------------------------------------------------------------------------

    diot@diot:~$ docker node ls
    ID                           HOSTNAME  STATUS    AVAILABILITY   MANAGER STATUS   ENGINE VERSION
    m77esfb3sm7deh0hru8fae6ke *  diot      Ready     Active         Leader           20.10.23
    rfxv2veuqcwoh9ou6yqam2clr    diot      Down      Active                         20.10.23
    4pmc4b04xifge30elwp6hyvdu    diot      Unknown   Active                          20.10.23
    qpfy8v9pa1cug1nr9w0ph0hx4    diot      Ready     Active                          20.10.23
    xfqavu8x2vh17q19tjvb1c2b0    localhost Ready     Active                          20.10.23
    
    
    diot@diot:~$ docker service ls
    ID             NAME         MODE         REPLICAS   IMAGE           PORTS
    erye0rdugrve   helloworld   replicated   7/5        alpine:latest   

--------------------------------------------------------------------------------------------------------
