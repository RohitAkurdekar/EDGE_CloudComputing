    diot@diot:~/<.dir>$ git init 

    hint: Using 'master' as the name for the initial branch. This default branch name
    hint: is subject to change. To configure the initial branch name to use in all
    hint: of your new repositories, which will suppress this warning, call:
    hint: 
    hint:   git config --global init.defaultBranch <name>
    hint: 
    hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
    hint: 'development'. The just-created branch can be renamed via this command:
    hint: 
    hint:   git branch -m <name>
    Initialized empty Git repository in /home/diot/<.dir>/.git/

---------------------------------------------------------------------------------------------------------

    diot@diot:~/<.dir>$ git status 
    On branch master

    No commits yet

    nothing to commit (create/copy files and use "git add" to track)

-----------------------------------------------------------------------------------------------

    diot@diot:~/<.dir>$ git config --list 
    user.name=RohitAkurdekar
    user.email=rakurdekar@gmail.com
    core.repositoryformatversion=0
    core.filemode=true
    core.bare=false
    core.logallrefupdates=true

---------------------------------------------------------------------------------------------------

    diot@diot:~/<.dir>$ git remote add origin https://github.com/RohitAkurdekar/gitdemo1.git
    diot@diot:~/<.dir>$ git config --list 
    user.name=RohitAkurdekar
    user.email=rakurdekar@gmail.com
    core.repositoryformatversion=0
    core.filemode=true
    core.bare=false
    core.logallrefupdates=true
    remote.origin.url=https://github.com/RohitAkurdekar/gitdemo1.git
    remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*

---------------------------------------------------------------------------------------------------

    diot@diot:~/<.dir>$ git status 
    On branch master

    No commits yet

    nothing to commit (create/copy files and use "git add" to track)

---------------------------------------------------------------------------------------------------

    diot@diot:~/<.dir>$ git pull origin master
    remote: Enumerating objects: 4, done.
    remote: Counting objects: 100% (4/4), done.
    remote: Compressing objects: 100% (3/3), done.
    remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
    Unpacking objects: 100% (4/4), 4.49 KiB | 4.49 MiB/s, done.
    From https://github.com/RohitAkurdekar/gitdemo1
    * branch            master     -> FETCH_HEAD
    * [new branch]      master     -> origin/master

---------------------------------------------------------------------------------------------------

    diot@diot:~/<.dir>$ git add .
    diot@diot:~/<.dir>$ git commit -m "Hello"
    [master e710158] Hello
    1 file changed, 1 insertion(+)
    create mode 100644 HelloWorld.py

    diot@diot:~/<.dir>$ git push origin master 
    Enumerating objects: 4, done.
    Counting objects: 100% (4/4), done.
    Delta compression using up to 12 threads
    Compressing objects: 100% (2/2), done.
    Writing objects: 100% (3/3), 324 bytes | 324.00 KiB/s, done.
    Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
    To https://github.com/RohitAkurdekar/gitdemo1.git
      fce8c14..e710158  master -> master
    
---------------------------------------------------------------------------------------------------
    
    diot@diot:~/<.dir>$ git branch 
    * master
    diot@diot:~/<.dir>$ git status 
    On branch master
    nothing to commit, working tree clean
    diot@diot:~/<.dir>$ git checkout -b rohit
    Switched to a new branch 'rohit'
    diot@diot:~/<.dir>$ git branch 
      master
    * rohit
    diot@diot:~/<.dir>$ ls
    HelloWorld.py  LICENSE  README.md

---------------------------------------------------------------------------------------------------

    diot@diot:~/<.dir>$ git add .

    diot@diot:~/<.dir>$ git commit -m "Rohit"
    [rohit 772d847] Rohit
    1 file changed, 3 insertions(+), 1 deletion(-)
    
    diot@diot:~/<.dir>$ git push origin rohit 
    Enumerating objects: 5, done.
    Counting objects: 100% (5/5), done.
    Delta compression using up to 12 threads
    Compressing objects: 100% (2/2), done.
    Writing objects: 100% (3/3), 333 bytes | 333.00 KiB/s, done.
    Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
    remote: 
    remote: Create a pull request for 'rohit' on GitHub by visiting:
    remote:      https://github.com/RohitAkurdekar/gitdemo1/pull/new/rohit
    remote: 
    To https://github.com/RohitAkurdekar/gitdemo1.git
    * [new branch]      rohit -> rohit
    
---------------------------------------------------------------------------------------------------
    
    diot@diot:~/<.dir>$ git checkout master 
    Switched to branch 'master'
    diot@diot:~/<.dir>$ git checkout rohit 
    Switched to branch 'rohit'


---------------------------------------------------------------------------------------------------

    diot@diot:~/<.dir>$ git checkout master 
    Switched to branch 'master'

    diot@diot:~/<.dir>$ git merge rohit 
    Updating e710158..772d847
    Fast-forward
    HelloWorld.py | 4 +++-
    1 file changed, 3 insertions(+), 1 deletion(-)


---------------------------------------------------------------------------------------------------

    diot@diot:~/<.dir>$ git checkout rohit 
    Switched to branch 'rohit'
    
    diot@diot:~/<.dir>$ git add .
    
    diot@diot:~/<.dir>$ git commit -m "Akurdekar"
    [rohit 088a538] Akurdekar
    1 file changed, 3 insertions(+), 1 deletion(-)

    diot@diot:~/<.dir>$ git restore --staged HelloWorld.py
    
    diot@diot:~/<.dir>$ git status 
    
    On branch rohit
    nothing to commit, working tree clean
    
---------------------------------------------------------------------------------------------------
    
    diot@diot:~/<.dir>$ git add .
    
    diot@diot:~/<.dir>$ git status 
    On branch rohit
    nothing to commit, working tree clean
    
    diot@diot:~/<.dir>$ git add .
    
    diot@diot:~/<.dir>$ git status 
    On branch rohit
    Changes to be committed:
      (use "git restore --staged <file>..." to unstage)
            modified:   HelloWorld.py

    diot@diot:~/<.dir>$ git restore --staged HelloWorld.py
    diot@diot:~/<.dir>$ git status 
    On branch rohit
    Changes not staged for commit:
      (use "git add <file>..." to update what will be committed)
      (use "git restore <file>..." to discard changes in working directory)
            modified:   HelloWorld.py

    no changes added to commit (use "git add" and/or "git commit -a")
    
---------------------------------------------------------------------------------------------------
    
    diot@diot:~/<.dir>$ cat HelloWorld.py 
    print("Hello")

    print("Rohit")

    print("Akurdekar")

    print("diot")
    
-------------------------------------------------------------------------------------------------    
    
    diot@diot:~/<.dir>$ git add . 

    diot@diot:~/<.dir>$ git commit -m "diot"
    [rohit 0d86f23] diot
    1 file changed, 3 insertions(+), 1 deletion(-)

    diot@diot:~/<.dir>$ git push  origin rohit 
    Enumerating objects: 8, done.
    Counting objects: 100% (8/8), done.
    Delta compression using up to 12 threads
    Compressing objects: 100% (6/6), done.
    Writing objects: 100% (6/6), 629 bytes | 629.00 KiB/s, done.
    Total 6 (delta 1), reused 0 (delta 0), pack-reused 0
    remote: Resolving deltas: 100% (1/1), done.
    To https://github.com/RohitAkurdekar/gitdemo1.git
      772d847..0d86f23  rohit -> rohit
    
    diot@diot:~/<.dir>$ git checkout master 
    Switched to branch 'master'
    
    diot@diot:~/<.dir>$ git checkout rohit 
    Switched to branch 'rohit'
    
    diot@diot:~/<.dir>$ 

---------------------------------------------------------------------------------------------------

  2023, Rohit Akurdekar.




  i-Max485 is a MODBUS gateway which receives data over MODBUS protocol and uploads data to server over MQTT protocol. Server provides UI to access data.Technolgy used:- MODBUS, MQTT, Angular Js, MongoDB, Container, Web programming