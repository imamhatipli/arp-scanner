from scapy.all import ARP, Ether, srp
import argparse
import pyfiglet
from colorama import *
import os
banner = pyfiglet.figlet_format("Arp - Scan")
if os.getuid() != 0:
    print("please run to root user")
    print(Fore.BLUE + banner)
    exit()
print(Fore.BLUE+banner)
print("Example: 192.168.1.1/24")
#target_ip = "192.168.16.1/24"
target_ip = input("subnet: ")
arp = ARP(pdst=target_ip)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether/arp
result = srp(packet, timeout=3, verbose=0)[0]
clients = []
for sent, received in result:
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

print("Available devices in the network:")
print("IP" + " "*18+"MAC")
for client in clients:
    print("{:16}    {}".format(client['ip'], client['mac']))