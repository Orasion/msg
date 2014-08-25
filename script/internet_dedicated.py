#!/usr/bin/python
### v1.1
### Front-End Script by Ndaru
### Mikrotik Script by Yudhis
### Pyperclip Module by Coffeeghost. Source bisa di download di http://coffeeghost.net/2010/10/09/pyperclip-a-cross-platform-clipboard-module-for-python/

import os, pyperclip, sys

# Bersihin layar dulu
os.system('cls' if os.name == 'nt' else 'clear')

print "\n"
print "-" * 40
print "|" + " " * 38 + "|"
print "| MIKROTIK SCRIPT : INTERNET DEDICATED |"
print "|      Front End Script by Ndaru       |"
print "|      Mikrotik Script by Yudhis       |"
print "|" + " " * 38 + "|"
print "-" * 40

# Form isian
client_name     = raw_input("Nama Klien : ")
ip_wan          = raw_input("IP Address WAN/subnet [co. 103.3.213.70/29] : ")
gateway_wan     = raw_input("IP Address Gateway WAN : ")

need_bridge     = raw_input("Apakah LAN akan di bridge ? [y/n] : ")

identity_skrip = '''
# Setting identity router
/system identity set name=(nama "%s")
# Setting user password : Tambahkan user reja dan disable user admin
/user add name=reja password=reja@oke group=full
/user disable number=0
''' % (client_name)

wan_skrip = '''
# Setting ip address WAN
/ip address add address=(address "%s") interface=ether2 disabled=no
''' % (ip_wan)

network_skrip = '''
# Setting DNS Server
/ip dns set server=8.8.8.8,8.8.4.4 allow-remote-requests=no

# Setting firewall NAT
/ip firewall nat add chain=srcnat action=masquerade

# Setting default route
/ip route add dst-address=0.0.0.0/0 gateway=%s
''' % (gateway_wan)

if need_bridge == "y":
        # bridge dah
        print "\nPort ether3-ether5 akan di bridge"
        ip_bridge       = raw_input("IP Address Bridge/subnet [co. 192.168.1.1/24] : ")
        bridge_skrip    = '''
# Buat interface bridge dan tambahkan ether3-ether5 secara rekursif
:local myPort "ether"
/interface bridge add name=Lan disabled=no
:for a from 3 to 5 do={/interface bridge port add interface=(interface $myPort.$a) bridge=Lan}

# Setting ip address bridge
/ip address add address=(address "%s") interface=Lan disabled=no
''' % (ip_bridge)
        skrip = identity_skrip + wan_skrip + bridge_skrip + network_skrip

elif need_bridge == "n":
        print "\nPort ether5 akan digunakan sebagai port LAN"
        ip_lan          = raw_input("IP Address LAN [co. 192.168.1.1/24] : ")
        lan_skrip       = '''
# Setting ip address LAN
/ip address add address=(address "%s") interface=ether5 disabled=no
''' % (ip_lan)
        skrip = identity_skrip + wan_skrip + lan_skrip + network_skrip

else:
        # Orang gila jawabnya beda
        sys.exit("Yah, malah milih yang lain. Gw keluar nih!!!")

print "\n"
print "*************************"
print "*    Generated Skrip    *"
print "*************************"

print skrip

print "\n*************************"
print "*     End Of Script     *"
print "*************************"


# Skrip berhasil dibuat, Copy ke clipboard atau keluar
print "Skrip berhasil dibuat. Tekan Enter untuk copy ke clipboard atau e untuk keluar skrip"
pilihan = raw_input("?")

if pilihan == "":
        # Copy to clipboard
        pyperclip.copy(skrip)
        spam = pyperclip.paste
        sys.exit("\nSkrip berhasil dicopy ke clipboard")
elif pilihan == "e":
        sys.exit("Yaudah kalo gak mau dicopy\n")
else:
        sys.exit("Yah, malah milih yang lain. Terserah lah!!!")
