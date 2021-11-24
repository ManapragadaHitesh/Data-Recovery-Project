import subprocess
import string
from ctypes import windll
import sys, os

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1
    return drives

print("------------------------")
print(" Welcome to Disk Imager ")
print("------------------------")
print()

print("[+] Available Drives to Scan are:")
drives = get_drives()
for drive in drives:
    print("\t", drive,":","\\", sep="")

while(True):
    option = input("\n[+] Select a drive to image:")
    if option.strip()[0].upper() in drives:
        break
    print("[-] Wrong Drive! Enter Again")

while(True):
    path = input("[+] Select destination drive where you want to save the image:")
    if (path.strip()[0].upper() in drives) and (path.strip()[0].upper() != option.strip()[0].upper()):
        break
    print("[-] Drive does not exist or source and destination drives cannot be same. Enter Again!")

print("[+] Imaging Under Progress")
print("[+] Please wait until process completes")

bb_path = '"' + resource_path("busybox.exe") + '"'
command = bb_path + " dd if=\\\.\{}: of={}:\{}_image.dd bs=512k".format(option.upper(),path.upper(),option.upper())
#print(command)
proc = subprocess.Popen(command, stdin = subprocess.PIPE, shell = False, stdout=subprocess.DEVNULL)
stdout, stderr = proc.communicate()
print("[+] Imaging finished! File saved at {}:\{}_image.dd".format(path.upper(),option.upper()))
#subprocess.check_output(command, shell = True, stderr= subprocess.STDOUT)
