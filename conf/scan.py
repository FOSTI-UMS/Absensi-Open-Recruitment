import cv2
import time
import base64
from conf.text import TextColor

FILENAME = "presence.csv"

class QRCodeInvalidError(Exception):
	def __init__(self, message = "Cannot recognize QR Code!"):
		formatted_message = "QRCodeInvalid: " + message
		self.message = formatted_message
		super().__init__(self.message)

class ScannerConnectionError(Exception):
	def __init__(self, message = "Cannot connect to scanner!"):
		formatted_message = "ScannerConnectionError: " + message
		self.message = formatted_message
		super().__init__(self.message)

def init_scanner(capture):
	"""Initialize QR Code Scanner from cv2 Video Capture"""
	ret, frame = capture.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	image = gray

	scanner = cv2.QRCodeDetector()
	value, points, straight_qrcode = scanner.detectAndDecode(image)
	return frame, value

def extract_qrdata(data):
	"""Extract QR Code Data from zbar scanner"""
	try:
		decode_msg = base64.b64decode(data).decode('utf-8')			
		qrsp = decode_msg.split('/')
	except:
		raise QRCodeInvalidError("Cannot decode qrcode!")

	if len(qrsp) != 4:
		raise QRCodeInvalidError("Data length is not valid!")

	student_id = qrsp[0]
	name = qrsp[1]
	email = qrsp[2]
	valid = qrsp[3] == "OPREC"
	presence_date = time.strftime('%Y-%m-%d')
	presence_time = time.strftime('%H:%M:%S')

	if not valid:
		raise QRCodeInvalidError()

	return student_id, name, email, presence_date, presence_time

def create_file():
	"""Create csv file if not exists"""
	try:
		with open(FILENAME, 'x'):
			pass
	except:
		pass

def already_presence(student_id):
	"""Check if student already presence or not"""
	presence_exist = False
	create_file()
	with open(FILENAME, "r") as f:
		text = f.readline()
		while text:
			presence_data = text.split(';')
			if student_id == presence_data[0]:
				presence_exist = True
				break
			text = f.readline()
	return presence_exist

def append_presence(student_id, name, email, date, time):
	"""Append presence data to csv file"""
	create_file()
	with open(FILENAME, "a") as f:
		f.write(student_id + ";" + name + ";" + email + ";" + date + ";" + time + "\n")

def frame_put_text(frame, text):
	"""Put text to video frame"""
	cv2.putText(frame, text, (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 2)

def print_logging(text_color, message):
	"""Print logging message to terminal"""
	print(f"{text_color}{message}{TextColor.END}")

def scanner_loop(url):
	try:
		print(f"{TextColor.YELLOW}[SCANNER] Loading...{TextColor.END}")
		cap = cv2.VideoCapture(url)

		info_displayed = False
		
		while(True):
			frame, value = init_scanner(cap)
			if not info_displayed:
				print(f"{TextColor.GREEN}[SCANNER] Connection success!{TextColor.END}")
				print(f"{TextColor.BOLD}[SCANNER] Press 'q' on window frame to exit!{TextColor.END}")
				info_displayed = True

			if value:
				try:
					student_id, name, email, date, time = extract_qrdata(value)

					if not already_presence(student_id):
						append_presence(student_id, name, email, date, time)
						frame_put_text(frame, "Presence success !")
						print_logging(TextColor.GREEN, f"[SCANNER] Presence success! {student_id} {name}")
					else:
						frame_put_text(frame, "Already presence !")
						print_logging(TextColor.BLUE, f"[SCANNER] Already presence! {student_id} {name}")			
				except Exception as e:
					frame_put_text(frame, "Invalid !")
					print(f"{TextColor.RED}[ERROR] {e}{TextColor.END}")

			cv2.imshow('FOSTI UMS Presence Scanner', frame)
			# Press 'q' on frame to exit program
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break

		cap.release()
		cv2.destroyAllWindows()
	except Exception as e:
		raise ScannerConnectionError()
