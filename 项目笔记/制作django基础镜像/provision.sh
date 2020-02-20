#!/bin/bash

#python的一些依赖



#python3.7
yum install -y python==3.7

#pip3

#django2.0.2

pip3 install -y django==2.0.2

pip3 install -r requirements.txt
python3 manage.py runserver 0.0.0.0:8000
