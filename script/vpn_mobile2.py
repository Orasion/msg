#!/usr/bin/python
### v0.1
### Front-End Script by Ndaru (orasionseis@gmail.com)
### Mikrotik Script by Yudhis (yudhistira.anggi@gmail.com)
### Pyperclip Module by Coffeeghost. Source code : http://coffeeghost.net/2010/10/09/pyperclip-a-cross-platform-clipboard-module-for-python/

import os, sys, pyperclip, linecache

# Clear Screen
os.system('cls' if os.name == 'nt' else 'clear')

print "L2TP Client using 3G Modem"
# PPP Config
ppp_interface   = raw_input("Interface PPP Name : ")
apn             = raw_input("APN : ")
dial            = raw_input("Dial Number [leave empty for default *99#] : ")
if dial == "":
    dial = "*99#"
else:
    dial = dial
configPPP           = linecache.getline('script.txt', 9) % (ppp_interface, apn, dial)
# Route IP LNS to ppp
ip_lns          = raw_input("IP LNS : ")
configLNSRoute      = linecache.getline('script.txt', 11) % (ip_lns, ppp_interface)
# L2TP VPN Config
l2tp_interface  = raw_input("Inteface L2TP Name : ")
vpn_user        = raw_input("VPN User : ")
vpn_pass        = raw_input("VPN pass : ")
configL2TP          = linecache.getline('script.txt', 13) % (l2tp_interface, ip_lns, vpn_user, vpn_pass)
# Config Bridge
bridge_interface = raw_input("Interface Bridge Name : ")
bridge_port_start= raw_input("Bridge port from ether : ")
bridge_port_end  = raw_input("to ether : ")
configRoute         = linecache.getline('script.txt', 15) % (l2tp_interface)
configBridge        = linecache.getline('script.txt', 17) % (bridge_interface, bridge_port_start, bridge_port_end, bridge_interface)
# Config LAN
ip_bridge       = raw_input("IP Address Bridge / subnet [xxx.xxx.xxx.xxx/xx] : ")
configLAN           = linecache.getline('script.txt', 19) % (ip_bridge, bridge_interface)
# Config DNS
ip_dns          = raw_input("DNS [separate by comma for multiple] : ")
configDNS           = linecache.getline('script.txt', 21) % (ip_dns)
# Identity, user, pass
client_name     = raw_input("Client Name : ")
adm_user        = raw_input("New Administrative user : ")
adm_pass        = raw_input("New password : ")
configIdentity      = linecache.getline('script.txt', 23) % (client_name, adm_user, adm_pass)
script  = configPPP + configLNSRoute + configL2TP + configRoute + configBridge + configLAN + configDNS + configIdentity
print "\n"
print "*************************"
print "*    Generated Skrip    *"
print "*************************"
print script
print "\n*************************"
print "*     End Of Script     *"
print "*************************"
print "Script generated. Press Enter to copy or e to exit"
choice = raw_input("?")
if choice == "":
        # Copy to clipboard
        pyperclip.copy(script)
        spam = pyperclip.paste
        sys.exit("\nCopied to clipboard")
elif pilihan == "e":
        sys.exit("Exiting\n")
else:
        sys.exit("Unexpected user input. Exiting")
