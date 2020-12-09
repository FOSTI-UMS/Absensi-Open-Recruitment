#Zbar is not supported now using zbar-py
import time
import math
from sys import argv
import os
# try:
import tkinter
from tkinter import messagebox
from subprocess import call
import zbar
import csv
import shutil
# except ImportError:
	#os.system("bash conf/req.sh")
	#try:
      # import Tkinter
		# import tkMessageBox
		# from subprocess import call
		# import zbar
		# import csv
		# import shutil
	# except ImportError:
	# 	exit()

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

os.system("clear")
def cekvid():
   import subprocess
   #viddev = subprocess.check_output('ls /dev | grep video', shell=True)
   viddev = "video0\nvideo1\n"
   print(viddev)
   viddev = viddev.split('\n')
   print(color.BOLD + color.YELLOW + "Perangkat tersedia, "+str(len(viddev)-1)+":\n" + color.END)
   nomer = 0
   for i in viddev:
      print(color.BOLD + color.UNDERLINE + color.CYAN + i + color.END)
   a = input(color.BOLD + color.BLUE + "Pilih perangkat(e.g. video1. quit/exit to close): " + color.END)
   keluar = ["quit", "QUIT", "q", "Q", "Quit", "Exit", "exit", "EXIT"]
   if a in keluar:
   	print(color.BOLD + color.GREEN + "Good Bye!!" + color.END)
   	exit()
   if a in viddev:
      return a
   else:
      print(color.BOLD + color.RED + "Perangkat ga ada NGACO!!" + color.END+"\n\n")
      cekvid()

prg = cekvid()
os.system("clear")
# if (len(argv) == 1):
#    	print color.BOLD+color.GREEN+"How to use it: python run.py argument\n(e.g. python run.py /dev/video1)"
# 	print color.BOLD+color.RED+"Use Tab"
# 	exit()


print(color.BOLD + color.UNDERLINE + color.GREEN + "\n\t\tAbsensi Open Recruitment FOSTI UMS" + color.END)
print(color.RED + "\t\t\tCopyright : FOSTI UMS" + color.END)
print("\n")

root = tkinter.Tk()

file = open("Oprec.csv", "w")
file.write("Nama,NIM,ID,Waktu\n")
file.close()

# x = open("Oprec.csv")
# x.readline()
# baca = csv.reader(x)

# isi = []

root.title("Absensi Oprec")

def absenCallBack():
   os.system("python3 conf/absensi.py /dev/"+prg)
	

B = tkinter.Button(root, text ="Absen", command = absenCallBack, height = 10, width = 30)
def on_closing():
   if messagebox.askokcancel("Selesai", "Sudah selesai?"):
      x=str( time.strftime('%A. %d %B %Y - Pukul %H.%M WIB'))
      os.makedirs( r'ABSEN OPEN RECRUITMENT - %s'%x)
      shutil.move('Oprec.csv', 'ABSEN OPEN RECRUITMENT - %s'%x)
      print(color.BOLD + color.GREEN + "\t\t\tTerima kasih!!")
      root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
B.pack()
B.config(bg='black', fg='red')
B.config(font=('Courier', 20, 'bold'))
root.mainloop()
