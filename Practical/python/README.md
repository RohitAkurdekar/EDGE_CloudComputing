# Dockerfile instruction

<h2>ADD instruction</h2>

Add file from current directory to container directory

-------------------------------------------------------------------------------------------------
<h2>WORKDIR instruction</h2>

Create and set a directory as a working directory.



-----------------------------------------------------------------------------------------------
    
    diot@diot:~/$ sudo docker build -t pythondemo:v2 .

    Sending build context to Docker daemon  3.072kB
    Step 1/5 : FROM python:3.10.9-alpine3.17
    ---> c8b069641107
    Step 2/5 : LABEL developer="rohitakurdekar"
    ---> Using cache
    ---> 709831058b8b
    Step 3/5 : WORKDIR /myapp/pythondemo
    ---> Using cache
    ---> 77c84a9df6d9
    Step 4/5 : ADD . /myapp/pythondemo/
    ---> a7566ce04d41
    Step 5/5 : CMD ["python","Helloworld.py"]
    ---> Running in bc0385cede63
    Removing intermediate container bc0385cede63
    ---> 4cb12ae2024c
    Successfully built 4cb12ae2024c
    Successfully tagged pythondemo:v2
    
    # ------------------------------------------------------------------------------------------

    diot@diot:~/$ sudo docker run --name hellopythondemo pythondemo:v2
    Hello from py container

------------------------------------------------------------------------------------------------------