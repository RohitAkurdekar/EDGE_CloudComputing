# Save and load commands

Save command

    $ sudo docker save <image_name:tag> > <tarfilename>.tar


Load command

    $ sudo docker save <image_name:tag> > <tarfilename>.tar



-------------------------------------------------------------------------

Example,

    diot@diot:~/$ sudo docker save ubuntu:mqttbrokerV0 > ubuntu_mqttbrokerV0.tar
    

    diot@diot:~/$ ls
    README.md  ubuntu_mqttbrokerV0.tar

-------------------------------------------------------------------------------------------------

    diot@diot:~/$ sudo docker load < ~/Downloads/alpine\ diothello.tar 
    
    ec34fcc1d526: Loading layer  5.811MB/5.811MB
    a2dbe67a3ba1: Loading layer  2.472MB/2.472MB
    Loaded image: alpine:diothello
    
-------------------------------------------------------------------------------------------------

    diot@diot:~/$ docker images 

    REPOSITORY               TAG                  IMAGE ID       CREATED         SIZE
    alpine                   diothello            ddbe4a5d292c   7 days ago      7.99MB


-------------------------------------------------------------------------------------------------------
2023, Rohit Akurdekar.