# DNN based Image Recognition of SKT
face recognition lecture @ SNU

## Practice Environment
* ubuntu 18.04 64bit (recommanded)
    * [Under windows 10 home, this practice is avialable via docker](./setting/docker_setting.md)
* python 2.7 (recommanded)

## Install Depedencies
* python 2.7
* pip
* opencv
* install ex. under ubuntu
~~~
apt-get update
apt-get install python2.7-dev python-pip
pip install -U pip==9.0.3
apt-get update
apt-get install python-numpy libopencv-dev python-opencv git
pip install requests
cd git
git clone https://github.com/junheeheu/skt_ai_lecture2019.git
~~~

## Lecture Code Download
* connect to the container 'lecture'.
~~~
mkdir git
cd git
git clone https://github.com/junheeheu/skt_ai_lecture2019.git
~~~

## Lectures
* [Chapter 1. How to load image using opencv.](./lecture/chap1.md)