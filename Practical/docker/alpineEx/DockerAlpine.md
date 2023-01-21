# docker alpine os

Dockerfile

    # Alpine

    FROM alpine
    LABEL developer="rakurdekar@gmail.com"
    RUN apk update
    RUN apk add net-tools
    # RUN echo "alpine worked...."
    CMD [ "echo","alpine worked" ]

-------------------------------------------------------------------------

__CLI__:

    $ docker build -t alpine:alpineex .

    Sending build context to Docker daemon  2.048kB
    Step 1/5 : FROM alpine
    latest: Pulling from library/alpine
    8921db27df28: Pull complete 
    Digest: sha256:f271e74b17ced29b915d351685fd4644785c6d1559dd1f2d4189a5e851ef753a
    Status: Downloaded newer image for alpine:latest
    ---> 042a816809aa
    Step 2/5 : LABEL developer="rakurdekar@gmail.com"
    ---> Running in e2695da977f1
    Removing intermediate container e2695da977f1
    ---> 0123f586d28f
    Step 3/5 : RUN apk update
    ---> Running in 4ec02ab6548d
    fetch https://dl-cdn.alpinelinux.org/alpine/v3.17/main/x86_64/APKINDEX.tar.gz
    fetch https://dl-cdn.alpinelinux.org/alpine/v3.17/community/x86_64/APKINDEX.tar.gz
    v3.17.1-47-ga69530033f [https://dl-cdn.alpinelinux.org/alpine/v3.17/main]
    v3.17.1-52-ge4b6fbc357 [https://dl-cdn.alpinelinux.org/alpine/v3.17/community]
    OK: 17813 distinct packages available
    Removing intermediate container 4ec02ab6548d
    ---> 15a904539f16
    Step 4/5 : RUN apk add net-tools
    ---> Running in ca526d07f7a8
    (1/2) Installing mii-tool (2.10-r0)
    (2/2) Installing net-tools (2.10-r0)
    Executing busybox-1.35.0-r29.trigger
    OK: 8 MiB in 17 packages
    Removing intermediate container ca526d07f7a8
    ---> 2f6c3f835392
    Step 5/5 : CMD [ "echo","alpine worked" ]
    ---> Running in b1c6055f59c9
    Removing intermediate container b1c6055f59c9
    ---> b26a6293bdad
    Successfully built b26a6293bdad
    Successfully tagged alpine:alpineex

    -----------------------------------------------------------------------------

    $ docker image ls

    REPOSITORY     TAG         IMAGE ID       CREATED          SIZE
    alpine         alpineex    b26a6293bdad   35 seconds ago   10.1MB
    ubuntu         myhello     4b4c0ce76c43   52 minutes ago   120MB