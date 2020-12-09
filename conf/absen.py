try:
	import cv2
	import zbar
	from sys import argv
	import time
	import numpy as np
	import base64
except:
	os.system("bash req.sh")
	try:
		import cv2
		import zbar
		from sys import argv
		import time
		import numpy as np
		import base64 
	except:
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

if len(argv) == 1:
	exit
else:
   device = argv[1]
print("Menggunakan "+device)
cap = cv2.VideoCapture(device)
temp = ""
while(True):
    # Capture frame-by-frame
	ret, frame = cap.read()
    # Our operations on the frame come here
	# ubah ke gray untuk memperingan zbar
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	ret = gray
	image = gray
	scanner = zbar.Scanner()
	results = scanner.scan(image)
	for result in results:
		try:
			#decode ke string
			decode_msg = base64.b64decode(result.data).decode('utf-8')
			#print(decode_msg)
			
			qrsp = decode_msg.split('/')
			if len(qrsp) !=4:
				print(color.BOLD + color.RED + "Invalid QR length ...[Error]" + color.END)
				ret = cv2.putText(frame, "Invalid QR length ...[Error]", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 2)
			nama = qrsp[2]
			nim = qrsp[1]
			unique_id = qrsp[3]
			valid = qrsp[0]
			waktu = time.strftime('Pukul %H.%M.%S WIB')
			if valid != qrsp[0]:
				print(color.BOLD + color.RED + "Invalid QR ...[Error]" + color.END)
				ret = cv2.putText(frame, "Invalid QR ...[Error]", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 2)
			if temp != decode_msg:
				#insert absensi
				data = open("Oprec.csv", "w")
				data.write(nama+","+nim+","+unique_id+","+waktu+","+"\n")
				data.close()
				temp = decode_msg
				print(" ...[SUCCESS]")
				ret = cv2.putText(frame, "Berhasil"+decode_msg, (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 2)
				print()
			else:
				ret = cv2.putText(frame, "Sudah Ter Absen", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 2)
		except TypeError:
			print(color.BOLD + color.RED + "Invalid QR ...[Error]"+color.END)
			print(decode_msg)
			ret = cv2.putText(frame, "Invalid QR ...[Error]", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 2)

	
	cv2.imshow('Scan QR Code FOSTI UMS',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
