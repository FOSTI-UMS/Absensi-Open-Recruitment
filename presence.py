from conf.text import TextColor
from conf.scan import scanner_loop
import subprocess
import platform

def clear_console():
    current_shell = platform.system().lower()
    
    if current_shell == "linux" or current_shell == "darwin":
        # For Bash (Linux/macOS)
        subprocess.call("clear", shell=True)
    elif current_shell == "windows":
        # For PowerShell (Windows)
        try:
            subprocess.call("Clear-Host", shell=True)
        except FileNotFoundError:
            # If PowerShell is not available, use cls (Windows Command Prompt)
            subprocess.call("cls", shell=True)

def show_banner():
    print(TextColor.BOLD + TextColor.UNDERLINE + TextColor.GREEN + "\n\t\tQR Presence Open Recruitment FOSTI UMS" + TextColor.END)
    print(TextColor.RED + "\t\t\tCopyright : FOSTI UMS" + TextColor.END)
    print("\n")

def choose_camera():
    print("Option : ")
    print("1. Scan using device webcam")
    print("2. Scan using IP webcam")
    print()
    
    option = input("Choose option: ")
    if option == "1":
        url = 0
    elif option == "2":
        url = input("Insert video url (ex: http://192.168.1.9:4747/video): ")
    else:
        url = None
        print("Invalid option!")

    return url

clear_console()
show_banner()
camera = choose_camera()
if not camera is None:
    try:
        scanner_loop(camera)
    except Exception as e:
        print(f"{TextColor.RED}[ERROR] {e}{TextColor.END}")
else:
    exit(127)