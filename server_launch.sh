#!/bin/bash
sudo apt-get install -y python3 python3-pip
sudo apt-get install -f flask

pip3 install flask flask-cors

# now run the python server as a daemon
nohup python3 server.py &
echo $! > server.pid