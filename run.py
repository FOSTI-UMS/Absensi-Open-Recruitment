#!/usr/bin/python
import time
import math
import os
try:
	import Tkinter
	import tkMessageBox
	import csv
	import shutil
	# import pwn
except ImportError:
	# print "Install module dulu, buka requirement.txt\n"
	os.system("bash req.sh")

root = Tkinter.Tk()

file = open("Oprec.csv", "w")
file.write("No,Nama,NIM\n")
file.close()

# x = open("Oprec.csv")
# x.readline()
# baca = csv.reader(x)

# isi = []

root.title("Absensi Oprec")

def absenCallBack():
   os.system("python absen.py")

B = Tkinter.Button(root, text ="Absen", command = absenCallBack, height = 10, width = 30)
def on_closing():
    if tkMessageBox.askokcancel("Selesai", "Sudah selesai?"):
		x=str( time.strftime('%A. %d %B %Y - Pukul %H.%M WIB'))
		os.makedirs( r'ABSEN OPEN RECUIREMENT - %s'%x)
		shutil.move('Oprec.csv', 'ABSEN OPEN RECUIREMENT - %s'%x)
		print "Terima kasih!!"
		root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
B.pack()
B.config(bg='black', fg='red')
B.config(font=('Courier', 20, 'bold'))
root.mainloop()