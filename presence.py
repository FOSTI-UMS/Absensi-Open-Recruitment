from conf.text import TextColor
from conf.scan import scanner_loop

print(TextColor.BOLD + TextColor.UNDERLINE + TextColor.GREEN + "\n\t\tQR Presence Open Recruitment FOSTI UMS" + TextColor.END)
print(TextColor.RED + "\t\t\tCopyright : FOSTI UMS" + TextColor.END)
print("\n")

url = input("Insert video url (ex: http://192.168.1.9:4747/video): ")
try:
    scanner_loop(url)
except Exception as e:
    print(f"{TextColor.RED}[ERROR] {e}{TextColor.END}")
