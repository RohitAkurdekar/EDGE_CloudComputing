# Docker

DockerFile &rArr; DockerImage &rArr; DockerContainer

__Docker container contains all the dependencies required.__


<h2>Commands to Install DOCKER engine</h2>

        $ curl -fsSL https://get.docker.com -o get-docker.sh
        $ DRY_RUN=1 sudo sh ./get-docker.sh


-----------------------------------------------------------------------------------
<h2>Create account on docker</h2>
<a href="https://hub.docker.com/signup">https://hub.docker.com/signup</a>

__Login from command line__:

        $ docker login

Enter valid credentials

username in small letter


To Login to docker using __specific username__

        $ docker login -u <username>



-----------------------------------------------------------------------------------
<h2>Execute docker</h2>

Test docker using:

        $ docker run hello-world



To create image from container

        $ docker commit <container_ID/container_Name> <Image_name>


PORT mapping of container

        $ docker run -it --name <containerID/containerName> -p <HostPort>:<ContainerPort> <ImageName>

To list all docker containers

        $ docker container ls -a
        $ docker ps -a

To list running docker containers

        $ docker container ls 
        $ docker ps 

To list images

        $ docker image ls

To run existing container

        $ docker start -i <containerName/containerID>

To attch CLI[BASH_SHELL] to running container

        $ docker attach -it <containerName/containerID>

To execute commands in running container

        $ docker exec -it <containerName/containerID> /bin/bash

To start container

        $ docker start <containerName/containerID>

To start container

        $ docker stop  <containerName/containerID>





------------------------------------------------------------------------------

__EXAMPLE__:

        $ docker run --name apacheserver -it apacheserver:v0

        $ service apache2 status

`*` apache2 is running

if not running 
        
        $ service apache2 start

Test using curl command on container CLI

--------------------------------------------------------------------------
root@2079e466f72d:/# curl http://< container_IP_Address>
 <!DOCTYPE html>
<html>
<head>
<title>Container server</title>
</head>
<body>

<h1>This is running in container</h1>
<p> This code is saved in  /var/www/html/index.html </p>

</body>
</html> 

----------------------------------------------------------------------------

        docker stop $(docker ps -q)

        docker start $(docker ps -a -q)

        git --hard reset HEAD^

----------------------------------------------------------------------

2023, Rohit Akurdekar