#python-container-experiment

If you ever wonder how to run various python versions in your docker containers and execute your script by them, you find answer here 

There are Docker files named accordingly to python version, eg. Dockerfile.py3 will create container with python3 and with simlink `pytho3 -> python` 

In the Docker file, you can specify which python version and which python libraries and tools you want to be installed in your image, e.g. I want to have installed `python3 python3-numpy python3-matplotlib`

One of the trick with such container as just python language, which is doing nothing after start is to keep it alive or in kind of infinite loop. One can done it with command:
 * `CMD exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"`

## How to build

 * `docker build -t python3:f25 -f Dockerfile.py3 .` - to build image with python3 
 * `docker build -t python2:f25 -f Dockerfile.py2 .` - to build image with python2 

## How to run the containers 

 * `docker run -v /home/mkocka/work/:/work --name py3 python3:f25 &`
 * `docker run -v /home/mkocka/work/:/work --name py2 python2:f25 &`

## How to execute your script in your container 
 
Using `-v /home/mkocka/work/:/work` You created a bind mount and you just need to have your script in mounted folder: `/home/mkocka/work/` in my case simple app.py which only print the python version. 

 * `docker exec -it py2 python /work/app.py` - app.py executed by python2
 * `docker exec -it py3 python /work/app.py` - app.py executed by python3

In my case, the output looks like this: 

`[mkocka@TheDude python-container-experiment]$ docker exec -it py2 python /work/app.py <br />
2.7.13 (default, Jan 12 2017, 17:59:37)  <br />
[GCC 6.3.1 20161221 (Red Hat 6.3.1-1)] <br />
[mkocka@TheDude python-container-experiment]$ docker exec -it py3 python /work/app.py <br />
3.5.2 (default, Sep 14 2016, 11:28:32)  <br />
[GCC 6.2.1 20160901 (Red Hat 6.2.1-1)]` <br />



