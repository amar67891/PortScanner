#!/usr/bin/python3

import socket 
import re
import ipaddress
import netaddr
from netaddr import *




print (""" 
 .d888888                                          
d8'    88                                          
88aaaaa88a 88d8b.d8b. 88d8b.d8b. .d8888b. 88d888b. 
88     88  88'`88'`88 88'`88'`88 88'  `88 88'  `88 
88     88  88  88  88 88  88  88 88.  .88 88       
88     88  dP  dP  dP dP  dP  dP `88888P8 dP       
ooooooooooooooooooooooooooooooooooooooooooooooooooo """)



port_range_pattern = re.compile("([0-9]+)-([0-9]+)")

port_min = 0 
port_max = 65535

open_ports = []

ip_add_entered = input("\nEnter the IP address of the Target: ")
while True:
    try:
        ip_addr = ipaddress.ip_address(ip_add_entered)
        print("\n** You have Entered a Valid IP address")
        break
    except:
         print("\n** Please Enter a Valid IP address")
         ip_add_entered = input("\nEnter the IP address of the Target: ")
    

while True:
    
    port_range = input("\nEnter port range [xx-xx]: ")
    port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break


for port in range(port_min, port_max + 1):

    try:
       
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            
            s.settimeout(0.5)
            s.connect((ip_add_entered, port))
            open_ports.append(port)

    except:

        pass


for port in open_ports:

    print(f"\n## Port {port} is open on {ip_add_entered} ##")