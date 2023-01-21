# Docker File

Instructions[Always in CAPITAL letter]

* FROM
* ADD
* MAINTAINER
* COPY
* CMD
* RUN

---------------------------------------------------------------------

Save file using 'DockerFile' without any extension

Steps to follow:

1. Create DockerFile
2. Write Instructions
3. Create the Docker Image[Build]

        $ docker build -t <imagename:tag/version> <DockerFilePath>

-t &rarr; tag name (referred as image name)


--------------------------------------------------------------------
Standard file descriptor

* STDIN  0
* STDOUT 1
* STDERR 2

------------------------------------------------------------------------

2023, Rohit Akurdekar