#!/usr/bin/python
### v1.0
### Front-End Script by Ndaru
### Mikrotik Script by Yudhis

import os, sys

# Clear Screen
os.system('cls' if os.name == 'nt' else 'clear')

print "\n"
print "-" * 38
print "|" + " " * 36 + "|"
print "| MIKROTIK SCRIPT GENERATOR LAUNCHER |"
print "|     Front End Script by Ndaru      |"
print "|     Mikrotik Script by Yudhis      |"
print "|" + " " * 36 + "|"
print "-" * 38

# Menu
print "\nAvailable Scripts : "
print "1. VPN Mobile"
print "2. Internet Dedicated"
pilihan = raw_input("Script to run ? ")

# Check input, only numbers allowed
try:
        pilihan = int(pilihan)
except ValueError:
        sys.exit("Please insert number from available scripts\n")

# Tentukan pilihan
if pilihan == 1:        
        execfile("vpn_mobile.py")
elif pilihan == 2:
        execfile("internet_dedicated.py")
else:
        print "Script no. " + str(pilihan) + " not available"

