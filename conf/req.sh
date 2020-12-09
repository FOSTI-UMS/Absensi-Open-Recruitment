#!/bin/bash

red=$'\e[1;31m'

grn=$'\e[1;32m'

blu=$'\e[1;34m'

mag=$'\e[1;35m'

cyn=$'\e[1;36m'

white=$'\e[0m'
echo -e $blu "Proses install modul bro"
echo -e $red "SABAR!!!"
echo -e $white
sleep 2
if ping -q -c 1 -W 1 8.8.8.8 >/dev/null; then
  pip3 install zbar-py
  pip3 install opencv-python
	sudo apt-get install zbar-tools -y
	sudo apt-get install python-tk -y
  echo -e $grn "Proses instalasi selesai!"
  echo -e $white
else
  echo -e $red "Konekin internet dulu bro"
  echo -e $white
fi
