import os

os.system("sudo freshclam")
myfile = input("file to be scanned: ")
pua = input("detect PUA (yes || no): ")
os.system("sudo clamscan --infected --recursive --allmatch --detect-pua=" + pua + " --phishing-sigs=yes --phishing-scan-urls=yes --alert-macros=yes " + myfile)

