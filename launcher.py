#!/usr/bin/python
### v1.0
### Front-End Script by Ndaru
### Mikrotik Script by Yudhis

import os, sys

# Bersihin layar dulu
os.system('cls' if os.name == 'nt' else 'clear')

print "\n"
print "-" * 38
print "|" + " " * 36 + "|"
print "| MIKROTIK SCRIPT GENERATOR LAUNCHER |"
print "|     Front End Script by Ndaru      |"
print "|     Mikrotik Script by Yudhis      |"
print "|" + " " * 36 + "|"
print "-" * 38

# Pilihan Menu
print "\nSkrip yang tersedia : "
print "1. VPN Mobile untuk CMN Store"
print "2. VPN Mobile"
print "3. Internet Dedicated"
pilihan = raw_input("Skrip yang ingin dijalankan ? ")

# Buat orang gila yang ngisi pake huruf
try:
        pilihan = int(pilihan)
except ValueError:
        sys.exit("Jangan gila dong!!! Masukin nomer aja\n")

# Tentukan pilihan
if pilihan == 1:        
        execfile("vpn_cmn.py")
elif pilihan == 2:
        execfile("vpn_mobile.py")
elif pilihan == 3:
        execfile("internet_dedicated.py")
else:
        print "gak ada no " + str(pilihan) + " tauuu"

