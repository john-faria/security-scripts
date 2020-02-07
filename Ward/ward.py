#!/usr/bin/env python

import os, sys


#SETTINGS==========================================================================================================================================================================================================
target = "/home/john/"
debug = ""
quietClam = ""
quietHunter = ""

#debug = "--verbose --archive-verbose --quiet"

'''
''' #add or remove a ' here to make it quiet or loud
quietClam = "--quiet" #comment to make scans loud
#quietHunter = "--report-warnings-only"
#'''

#==================================================================================================================================================================================================================

if(sys.argv[0] > 0):
    target = sys.argv[1]

#date = 

exclusions = "--exclude-dir=/sys/module/ --exclude-dir=/sys/bus/ --exclude-dir=/home/john/Projects/set/ --exclude-dir=/home/john/.cache/yay/snort/ --exclude-dir=/home/john/VirtualBox\ VMs/"


clamscanCommand = "sudo clamscan --bell --recursive --allmatch " + debug + quietClam + " --detect-pua=no --phishing-sigs=yes --phishing-scan-urls=yes --log=logs/most-recent.log --alert-macros=yes " + exclusions + " --max-filesize=120M " + target


#commands
print("Updating virus signatures")
os.system("sudo freshclam")

print("Begining scan of " + target)
os.system(clamscanCommand)

print("Starting rootkit hunt")
os.system("sudo rkhunter --check --logfile " + quietHunter + "  --skip-keypress")
os.system("cat gap.txt >> logs/most-recent.log; sudo cat /var/log/rkhunter.log >> logs/most-recent.log")
