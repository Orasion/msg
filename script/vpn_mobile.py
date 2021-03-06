#!/usr/bin/python
### v1.1
### Front-End Script by Ndaru (orasionseis@gmail.com)
### Mikrotik Script by Yudhis (yudhistira.anggi@gmail.com)
### Pyperclip Module by Coffeeghost. Source code : http://coffeeghost.net/2010/10/09/pyperclip-a-cross-platform-clipboard-module-for-python/

import os, sys, pyperclip

# Clear Screen
os.system('cls' if os.name == 'nt' else 'clear')

print "\n"
print "-" * 32
print "|" + " " * 30 + "|"
print "| MIKROTIK SCRIPT : VPN MOBILE |"
print "|   Front End Script by Ndaru  |"
print "|   Mikrotik Script by Yudhis  |"
print "|" + " " * 30 + "|"
print "-" * 32

# Identity and Dial Up Profile
client_name     = raw_input("Client Name : ")
dialup_profile  = raw_input("Dial Up Profile : ")

profile         = dialup_profile.split('@')
password        = profile[0]

dialup_skrip = '''
# Router Identity
/system identity set name=(name "%s")

# Setting Dial Up
/interface ppp-client add name=(name "Esia") phone=#777 user=(user "%s") password=(pass "%s") dial-on-demand=no use-peer-dns=no add-default-route=no disable=no
''' % (client_name, dialup_profile, password)

# IP Address and network
print "\nEther2 to Ether5 will be bridged and subnet /24 will be given"
ip_address      = raw_input("IP Address Bridge : ")
block           = ip_address.split('.')
ip_network      = int(block[3]) - 1
network         = block[0] + "." + block[1] + "." + block[2] + "." + str(ip_network)

# Specify DHCP Range based on IP Bridge
ip_host_start   = int(block[3]) + 1
ip_host_end     = int(block[3]) + 253
range_dhcp      = block[0] + "." + block[1] + "." + block[2] + "." + str(ip_host_start) + "-" + block[0] + "." + block[1] + "." + block[2] + "." + str(ip_host_end)

network_skrip   = '''
# Create bridge interface then add ether2 to ether5 recursively
:local myPort "ether"
/interface bridge add name=Lan disabled=no
:for a from 2 to 5 do={/interface bridge port add interface=(interface $myPort.$a) bridge=Lan}

# IP Bridge Configuration
/ip address add address=(address "%s/24") interface=Lan disabled=no

# DNS Server Configuration
/ip dns set server=8.8.8.8,8.8.4.4 allow-remote-requests=no

# NAT Configuration
/ip firewall nat add chain=srcnat action=masquerade

# DHCP Server Configuration
/ip pool add name=lan range=(address "%s")
/ip dhcp-server add name=lan interface=Lan address-pool=lan
/ip dhcp-server enable number=lan
/ip dhcp-server network add address=(address "%s/24") gateway=(gateway "%s") dns-server=8.8.8.8,8.8.4.4
''' % (ip_address, range_dhcp, network, ip_address)

route_skrip = '''
# Route Configuration
/ip route add dst-address=0.0.0.0/0 gateway=(gateway "Esia")
'''

# Permission script
permission_skrip = '''
# Setting user password : Tambahkan user reja dan disable user admin
/user add name=reja password=reja@oke group=full
/user disable number=0
'''

# Wifi Configuration
need_wifi       = raw_input("Need Wifi? [y/n] : ")
if need_wifi == "y":        
        # WIfi Network Configuration
        print "\nWifi will be /24 and network will be different than Wired LAN"
        ip_address_wifi = raw_input("IP Address Wifi : ")
        block_wifi      = ip_address_wifi.split('.')
        ip_network_wifi = int(block_wifi[3]) - 1
        network_wifi    = block_wifi[0] + "." + block_wifi[1] + "." + block_wifi[2] + "." + str(ip_network_wifi)

        # Specify DHCP Range based on IP Bridge
        ip_host_start_wifi   = int(block_wifi[3]) + 1
        ip_host_end_wifi     = int(block_wifi[3]) + 253
        range_dhcp_wifi      = block_wifi[0] + "." + block_wifi[1] + "." + block_wifi[2] + "." + str(ip_host_start_wifi) + "-" + block_wifi[0] + "." + block_wifi[1] + "." + block_wifi[2] + "." + str(ip_host_end_wifi)

        # Wifi Security Configuration
        print "\nWPA2 will be used"
        ssid            = raw_input("SSID Wifi : ")
        wpa_key         = raw_input("WPA Key : ")
        
        wifi_skrip = '''
# WLAN IP Address Configuration
/ip address add address=(address "%s/24") interface=wlan1 disabled=no
        
# Wifi Security Porfile Configuration
/interface wireless security-profiles add name=wpa2 authentication-types=wpa-psk,wpa2-psk mode=dynamic-keys unicast-ciphers=tkip group-ciphers=tkip wpa-pre-shared-key=%s wpa2-pre-shared-key=%s

# WLAN Interface Configuration
/interface wireless set numbers=0 security-profile=wpa2 disabled=no
/interface wireless set wlan1 ssid=%s band=2ghz-b/g/n mode=ap-bridge disabled=no

# WLAN DHCP Server Configuration
/ip pool add name=wlan range=(address "%s")
/ip dhcp-server add name=wlan interface=wlan1 address-pool=wlan
/ip dhcp-server enable number=wlan
/ip dhcp-server network add address=(address "%s/29") gateway=(gateway "%s") dns-server=8.8.8.8,8.8.4.4
''' % (ip_address_wifi, wpa_key, wpa_key, ssid, range_dhcp_wifi, network_wifi, ip_address_wifi)

        skrip = dialup_skrip + network_skrip + wifi_skrip + route_skrip + permission_skrip
elif need_wifi == "n":
        # No Need for Wifi
        skrip = dialup_skrip + network_skrip + route_skrip + permission_skrip
else:
        # Unexpected User Input. Exit
        sys.exit("Unexpected User Input. Exiting")

print "\n"
print "*************************"
print "*    Generated Skrip    *"
print "*************************"

print skrip

print "\n*************************"
print "*     End Of Script     *"
print "*************************"

# Script successfully generated
print "Script has successfully been made. Press Enter to copy or e to exit"
pilihan = raw_input("?")

if pilihan == "":
        # Copy to clipboard
        pyperclip.copy(skrip)
        spam = pyperclip.paste
        sys.exit("\nCopied to clipboard")
elif pilihan == "e":
        sys.exit("Exiting\n")
else:
        sys.exit("Unexpected user input. Exiting")
