#!/usr/bin/python
from sys import argv
from sys import exit
import time
import math
import os
import random

try:
	from subprocess import call
	import zbar
	import csv
	import shutil
except ImportError:
	# print "Install module dulu, buka requirement.txt"
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

# print color.BOLD + color.UNDERLINE + color.GREEN + "\t\tAbsensi Open Requirement FOSTI UMS" + color.END
# print color.RED + "\t\t\tCopyright : FOSTI UMS" + color.END
# print "\n"

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
# Font coloring

fontcolor = [color.PURPLE,color.CYAN,color.DARKCYAN,color.BLUE, color.GREEN, color.YELLOW]

for symbol in proc.results:
    # do something useful with results
    # print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data
	# nomer+=1
	qrsp = symbol.data.split('/')
	if len(qrsp) != 4:
		print color.BOLD + color.RED + "Invalid QR length ............................[Error]" + color.END
		break
	nama = qrsp[2]
	nim = qrsp[1]
	unique_id = qrsp[3]
	valid = qrsp[0]
	waktu = time.strftime('Pukul %H.%M.%S WIB')
	# data.write (str(nomer))
	# data.write (",")
	if valid != "Fosti_Oprec":
		print color.BOLD + color.RED + "Invalid QR ............................[Error]"
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

	# print "Selamat datang "+nama
	print color.BOLD + random.choice(fontcolor)+"Selamat datang "+ nama + "..........................[OK]"
	print