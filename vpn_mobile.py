#!/usr/bin/python
### v1.1
### Front-End Script by Ndaru
### Mikrotik Script by Yudhis
### Pyperclip Module by Coffeeghost. Source bisa di download di http://coffeeghost.net/2010/10/09/pyperclip-a-cross-platform-clipboard-module-for-python/

import os, sys, pyperclip

# Bersihin layar dulu
os.system('cls' if os.name == 'nt' else 'clear')

print "\n"
print "-" * 32
print "|" + " " * 30 + "|"
print "| MIKROTIK SCRIPT : VPN MOBILE |"
print "|   Front End Script by Ndaru  |"
print "|   Mikrotik Script by Yudhis  |"
print "|" + " " * 30 + "|"
print "-" * 32

# Identity dan Dial Up Profile
client_name     = raw_input("Nama Klien : ")
dialup_profile  = raw_input("Dial Up Profile : ")

profile         = dialup_profile.split('@')
password        = profile[0]

dialup_skrip = '''
# Setting identity router
/system identity set name=(nama "%s")

# Setting Dial Up
/interface ppp-client add name=(name "Esia") phone=#777 user=(user "%s") password=(pass "%s") dial-on-demand=no use-peer-dns=no add-default-route=no disable=no
''' % (client_name, dialup_profile, password)

# IP Address dan network
print "\nEther2 - Ether5 akan dibridge dan subnet akan dibuat /24"
ip_address      = raw_input("IP Address Bridge : ")
block           = ip_address.split('.')
ip_network      = int(block[3]) - 1
network         = block[0] + "." + block[1] + "." + block[2] + "." + str(ip_network)

# Tentukan IP DHCP Range berdasarkan IP Address
ip_host_start   = int(block[3]) + 1
ip_host_end     = int(block[3]) + 253
range_dhcp      = block[0] + "." + block[1] + "." + block[2] + "." + str(ip_host_start) + "-" + block[0] + "." + block[1] + "." + block[2] + "." + str(ip_host_end)

network_skrip   = '''
# Buat interface bridge dan tambahkan ether2-ether5 secara rekursif
:local myPort "ether"
/interface bridge add name=Lan disabled=no
:for a from 2 to 5 do={/interface bridge port add interface=(interface $myPort.$a) bridge=Lan}

# Setting ip address bridge
/ip address add address=(address "%s/24") interface=Lan disabled=no

# Setting DNS Server
/ip dns set server=8.8.8.8,8.8.4.4 allow-remote-requests=no

# Setting firewall NAT
/ip firewall nat add chain=srcnat action=masquerade

# Setting DHCP Server 
/ip pool add name=lan range=(address "%s")
/ip dhcp-server add name=lan interface=Lan address-pool=lan
/ip dhcp-server enable number=lan
/ip dhcp-server network add address=(address "%s/24") gateway=(gateway "%s") dns-server=8.8.8.8,8.8.4.4
''' % (ip_address, range_dhcp, network, ip_address)

route_skrip = '''
# Setting default route
/ip route add dst-address=0.0.0.0/0 gateway=(gateway "Esia")
'''

# Permission Skrip
permission_skrip = '''
# Setting user password : Tambahkan user reja dan disable user admin
/user add name=reja password=reja@oke group=full
/user disable number=0
'''

# Setting Wifi
need_wifi       = raw_input("Butuh Wifi? [y/n] : ")
if need_wifi == "y":        
        # Setting network Wifi
        print "\nWifi akan dibuat /24 dan memiliki network yang berbeda dengan Lan Kabel"
        ip_address_wifi = raw_input("IP Address Wifi : ")
        block_wifi      = ip_address_wifi.split('.')
        ip_network_wifi = int(block_wifi[3]) - 1
        network_wifi    = block_wifi[0] + "." + block_wifi[1] + "." + block_wifi[2] + "." + str(ip_network_wifi)

        # Tentukan IP DHCP Range berdasarkan IP Address
        ip_host_start_wifi   = int(block_wifi[3]) + 1
        ip_host_end_wifi     = int(block_wifi[3]) + 253
        range_dhcp_wifi      = block_wifi[0] + "." + block_wifi[1] + "." + block_wifi[2] + "." + str(ip_host_start_wifi) + "-" + block_wifi[0] + "." + block_wifi[1] + "." + block_wifi[2] + "." + str(ip_host_end_wifi)

        # Setting security Wifi
        print "\nWifi akan memakai WPA2"
        ssid            = raw_input("SSID Wifi : ")
        wpa_key         = raw_input("WPA Key : ")
        
        wifi_skrip = '''
# Setting IP Address Wlan
/ip address add address=(address "%s/24") interface=wlan1 disabled=no
        
# setting security profile wifi
/interface wireless security-profiles add name=wpa2 authentication-types=wpa-psk,wpa2-psk mode=dynamic-keys unicast-ciphers=tkip group-ciphers=tkip wpa-pre-shared-key=%s wpa2-pre-shared-key=%s

# Setting interface wlan
/interface wireless set numbers=0 security-profile=wpa2 disabled=no
/interface wireless set wlan1 ssid=%s band=2ghz-b/g/n mode=ap-bridge disabled=no

# Setting DHCP Server Wlan
/ip pool add name=wlan range=(address "%s")
/ip dhcp-server add name=wlan interface=wlan1 address-pool=wlan
/ip dhcp-server enable number=wlan
/ip dhcp-server network add address=(address "%s/29") gateway=(gateway "%s") dns-server=8.8.8.8,8.8.4.4
''' % (ip_address_wifi, wpa_key, wpa_key, ssid, range_dhcp_wifi, network_wifi, ip_address_wifi)

        skrip = dialup_skrip + network_skrip + wifi_skrip + route_skrip + permission_skrip
elif need_wifi == "n":
        # lewat
        skrip = dialup_skrip + network_skrip + route_skrip + permission_skrip
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
