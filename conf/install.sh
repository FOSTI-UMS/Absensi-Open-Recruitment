#!/bin/bash

red=$'\e[1;31m'
grn=$'\e[1;32m'
blu=$'\e[1;34m'
mag=$'\e[1;35m'
cyn=$'\e[1;36m'
ylw=$'\e[33m'

white=$'\e[0m'
echo -e $ylw "Installing modules..."
echo -e $white
sleep 2

if ping -q -c 1 -W 1 8.8.8.8 > /dev/null; then
  pip3 install zbar-py
  pip3 install opencv-python
  pip3 install opencv-python-headless
	sudo apt-get install zbar-tools -y
	sudo apt-get install python-tk -y
  echo -e $grn "Installation completed!"
  echo -e $white
else
  echo -e $red "Connection error, please check your network!"
  echo -e $white
fi
