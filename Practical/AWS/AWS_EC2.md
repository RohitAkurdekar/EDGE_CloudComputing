# EC2

Steps to use EC2

* Select service EC2
* Click on Launch instance
* Enter details
* Add security group
    * Download key file
* Launch instance
* Go to security groups
* Edit inbound rules
    * Add custom rules [port,ip,etc]
* Connect

-----------------------------------------------------------------------

Example, 

    diot@diot:~/$ ssh -i ./demo_cloud.pem ubuntu@43.205.206.35

    ubuntu@ip-172-31-34-50:~$ 

    ubuntu@ip-172-31-34-50:~$ exit 
    logout
    Connection to 43.205.206.35 closed.
