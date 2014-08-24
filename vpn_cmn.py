#!/usr/bin/python
### v1.1
### Front-End Script by Ndaru
### Mikrotik Script by Yudhis
### Pyperclip Module by Coffeeghost. Source bisa di download di http://coffeeghost.net/2010/10/09/pyperclip-a-cross-platform-clipboard-module-for-python/

import os, pyperclip, sys

# Bersihin layar dulu
os.system('cls' if os.name == 'nt' else 'clear')

print "\n"
print "-" * 60
print "|" + " " * 58 + "|"
print "| MIKROTIK SCRIPT : VPN CLIENT CITRA MITRA NUSANTARA STORE |"
print "|             Front End Script by Ndaru                    |"
print "|             Mikrotik Script by Yudhis                    |"
print "|" + " " * 58 + "|"
print "-" * 60

# Form isian
client_name = raw_input("Nama Klien : ")
ip_address = raw_input("LAN IP Address : ")

# Tentukan IP Network berdasarkan IP Address
# block = ip_address.split('.')
# ip_network = int(block[3]) - 1
# network = block[0] + "." + block[1] + "." + block[2] + "." + str(ip_network)

# Tentukan IP DHCP Range berdasarkan IP Address
# ip_host_start = int(block[3]) + 1
# ip_host_end = int(block[3]) + 5
# range_dhcp = block[0] + "." + block[1] + "." + block[2] + "." + str(ip_host_start) + "-" + block[0] + "." + block[1] + "." + block[2] + "." + str(ip_host_end)
# range_dhcp = block[0] + "." + block[1] + "." + block[2] + "." + str(ip_host_start)

print "\n"
print "*************************"
print "*    Generated Skrip    *"
print "*************************"

# Skrip Mikrotik
skrip = '''
:local myPort "ether"

# Buat interface bridge dengan nama "Lan" dan masukkan ether2-ether5 ke bridge
/interface bridge add name=Lan disabled=no
:for a from 2 to 5 do={/interface bridge port add \ interface=(interface $myPort.$a) bridge=Lan}

# Setting Dial Up
/interface ppp-client add name=(name "Esia") phone=#777 user=(user "%s@cmn.id") password=(pass "%s") dial-on-demand=no use-peer-dns=no add-default-route=no disable=no

# Setting DNS Server
/ip dns set server=8.8.8.8,8.8.4.4 allow-remote-requests=no

# Setting default route
/ip route add dst-address=0.0.0.0/0 gateway=(gateway "Esia")

# Setting ip address bridge
/ip address add address=(address "%s/30") interface=Lan disabled=no

# Setting firewall NAT
/ip firewall nat add chain=srcnat action=masquerade

# Setting identity router
/system identity set name=(nama "CMN Store")

# Setting user password : Tambahkan user reja dan disable user admin
/user add name=reja password=reja@oke group=full
/user disable number=0
''' % (client_name, client_name, ip_address)

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
