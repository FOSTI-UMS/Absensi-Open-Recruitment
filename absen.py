#!/usr/bin/python
from sys import argv
from sys import exit
import time
import math
import os

try:
	from subprocess import call
	import zbar
	import csv
	import shutil
	# import pwn
except ImportError:
	# print "Install module dulu, buka requirement.txt"
	os.system("bash req.sh")

#  Create csv and header
# file = open("Oprec.csv", "w")
# file.write("No,Nama,NIM\n")
# file.close()

# x = open("Oprec.csv")
# x.readline()
# baca = csv.reader(x)

# isi = []

data = open("Oprec.csv", "a")

# create a Processor
proc = zbar.Processor()
# configure the Processor
proc.parse_config('enable')
# initialize the Processor
device = '/dev/video0'
if len(argv) == 1:
	# print "Asking a argument"
	exit
else:
   device = argv[1]
proc.init(device)
# enable the preview window
proc.visible = True
# read at least one barcode (or until window closed)
proc.process_one()
# hide the preview window
proc.visible = False
# extract results
nomer = 0
for symbol in proc.results:
    # do something useful with results
    # print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data
	nomer+=1
	qrsp = symbol.data.split('/')
	nama = qrsp[1]
	nim = qrsp[0]
	data.write (str(nomer))
	data.write (",")
	data.write (nama)
	data.write (",")
	data.write (nim)
	data.write (",")
	data.write ("\n")
	data.close()

	print "Selamat datang "+nama