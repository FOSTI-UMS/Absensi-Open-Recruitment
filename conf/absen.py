#!/usr/bin/python2
from sys import argv
from sys import exit
import time
import math
import os
import random
import hashlib
import base64

try:
	from subprocess import call
	import zbar
	import csv
	import shutil
except ImportError:
	os.system("bash req.sh")
	try:
		from subprocess import call
		import zbar
		import csv
		import shutil
	except ImportError:
		exit()

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

data = open("Oprec.csv", "a")

# create a Processor
proc = zbar.Processor()
# configure the Processor
proc.parse_config('enable')
# initialize the Processor
device = '/dev/video0'
if len(argv) == 1:
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
# Font coloring

fontcolor = [color.PURPLE,color.CYAN,color.DARKCYAN,color.BLUE, color.GREEN, color.YELLOW]

vld = hashlib.md5()
vld.update("Fosti_Oprec")
valid = vld.hexdigest()

for symbol in proc.results:
    # do something useful with results
    # print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data
	try:
		# base64.b64decode(symbol.data)
		strdecode = base64.b64decode(symbol.data)
		qrsp = strdecode.split('/')
		if len(qrsp) != 4:
			print(color.BOLD + color.RED + "Invalid QR length ...[Error]" + color.END)
			break
		nama = qrsp[2]
		nim = qrsp[1]
		unique_id = qrsp[3]
		valid = qrsp[0]
		waktu = time.strftime('Pukul %H.%M.%S WIB')
		
		if valid != qrsp[0]:
			print(color.BOLD + color.RED + "Invalid QR ...[Error]")
			break
		data.write (nama)
		data.write (",")
		data.write (nim)
		data.write (",")
		data.write (unique_id)
		data.write (",")
		data.write (waktu)
		data.write (",")
		data.write ("\n")
		data.close()

		print(color.BOLD + random.choice(fontcolor)+"Welcome "+ nama + " ...[SUCCESS]")
		print()
	except TypeError:
		print(color.BOLD + color.RED + "Invalid QR ...[Error]"+color.END)
		exit()
