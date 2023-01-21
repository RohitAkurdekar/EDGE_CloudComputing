# docker ubuntu os


    ------------------ Dockerfile ------------------------
    FROM ubuntu:22.04 
    RUN apt update -y
    RUN apt install net-tools -y
    # RUN ifconfig
    RUN echo "Hello from Mogambo"


    ------------------ CLI[Terminal] ------------------------

    $ docker build -t ubuntu:myhello .

    Sending build context to Docker daemon  2.048kB
    Step 1/4 : FROM ubuntu:22.04
    ---> 6b7dfa7e8fdb
    Step 2/4 : RUN apt update -y
    ---> Running in ed30bd790f68
    Fetched 25.2 MB in 6s (4165 kB/s)
    Reading package lists...
    Building dependency tree...
    Reading state information...
    All packages are up to date.
    Removing intermediate container ed30bd790f68
    ---> e90a57da3ee7
    Step 3/4 : RUN apt install net-tools -y
    ---> Running in 63eabd4603ed

    Reading package lists...
    Building dependency tree...
    Reading state information...
    The following NEW packages will be installed:
    net-tools
    0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
    Step 4/4 : RUN echo "Hello from Mogambo"
    ---> Running in 98bc7bc52e09
    Hello from Mogambo
    Removing intermediate container 98bc7bc52e09
    ---> 4b4c0ce76c43
    Successfully built 4b4c0ce76c43
    Successfully tagged ubuntu:myhello

    -------------------------------------------------------------------

    $ docker image ls
    REPOSITORY     TAG         IMAGE ID       CREATED         SIZE
    ubuntu         myhello     4b4c0ce76c43   2 minutes ago   120MB
