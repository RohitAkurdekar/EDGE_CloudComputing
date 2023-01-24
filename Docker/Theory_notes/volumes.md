# Docker volumes

    docker run -it --restart always --name demo_ubuntu1 -v volume_demo:/diot/data ubuntu:20.04 
    root@0c33dd86dfd6:/# cd /diot/data/
    root@0c33dd86dfd6:/diot/data# touch hello.txt
    root@0c33dd86dfd6:/diot/data# echo "This data is stored in container" > hello.txt 
    root@0c33dd86dfd6:/diot/data# cat hello.txt 
    This data is stored in container
    root@0c33dd86dfd6:/diot/data# cat hello.txt 
    This data is stored in container.
    This data is written from host.
    root@0c33dd86dfd6:/diot/data# 

--------------------------------------------------------------------------------------

    diot@diot:~$ sudo su
    [sudo] password for diot: 
    root@diot:/home/diot# cd /var/lib/docker/volumes/
    root@diot:/var/lib/docker/volumes# cd 
    backingFsBlockDev  metadata.db        volume_demo/       
    root@diot:/var/lib/docker/volumes# cd volume_demo/
    root@diot:/var/lib/docker/volumes/volume_demo# ls
    _data
    root@diot:/var/lib/docker/volumes/volume_demo# cd _data/
    root@diot:/var/lib/docker/volumes/volume_demo/_data# ls
    root@diot:/var/lib/docker/volumes/volume_demo/_data# 
    root@diot:/var/lib/docker/volumes/volume_demo/_data# ls
    root@diot:/var/lib/docker/volumes/volume_demo/_data# ls
    hello.txt
    root@diot:/var/lib/docker/volumes/volume_demo/_data# cat hello.txt 
    This data is stored in container
    root@diot:/var/lib/docker/volumes/volume_demo/_data# nano hello.txt 
    root@diot:/var/lib/docker/volumes/volume_demo/_data# 

--------------------------------------------------------------------------------------------

    root@diot:~# cp /home/diot/Documents/Rohit/EDGE_Cloud/Docker/Theory_notes/volumes.md /var/lib/docker/volumes/volume_demo/_data/
    root@diot:~# 

--------------------------------------------------------------------------------------------

    root@0c33dd86dfd6:/diot/data# ls
    hello.txt  volumes.md


---------------------------------------------------------------------------------------------------
2023, Rohit Akurdekar