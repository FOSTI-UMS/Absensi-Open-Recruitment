#!/usr/bin/python
import time
import math
from sys import argv
import os
try:
	import Tkinter
	import tkMessageBox
	from subprocess import call
	import zbar
	import csv
	import shutil
except ImportError:
	os.system("bash conf/req.sh")
	try:
		import Tkinter
		import tkMessageBox
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
 
if (len(argv) == 1):
   	print color.BOLD+color.GREEN+"How to use it: python run.py argument\n(e.g. python run.py /dev/video1)"
	print color.BOLD+color.RED+"Use Tab"
	exit()


print color.BOLD + color.UNDERLINE + color.GREEN + "\n\t\tAbsensi Open Requirement FOSTI UMS" + color.END
print color.RED + "\t\t\tCopyright : FOSTI UMS" + color.END
print "\n"

root = Tkinter.Tk()

file = open("Oprec.csv", "w")
file.write("Nama,NIM,ID,Waktu\n")
file.close()

# x = open("Oprec.csv")
# x.readline()
# baca = csv.reader(x)

# isi = []

root.title("Absensi Oprec")

def absenCallBack():
   os.system("python conf/absen.py "+argv[1])
	

B = Tkinter.Button(root, text ="Absen", command = absenCallBack, height = 10, width = 30)
def on_closing():
    if tkMessageBox.askokcancel("Selesai", "Sudah selesai?"):
		x=str( time.strftime('%A. %d %B %Y - Pukul %H.%M WIB'))
		os.makedirs( r'ABSEN OPEN RECUIREMENT - %s'%x)
		shutil.move('Oprec.csv', 'ABSEN OPEN RECUIREMENT - %s'%x)
		print color.BOLD + color.GREEN + "\t\t\tTerima kasih!!"
		root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
B.pack()
B.config(bg='black', fg='red')
B.config(font=('Courier', 20, 'bold'))
root.mainloop()