#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created March 2019

@author: othornew
"""

import argparse
from datetime import datetime
from scapy.all import srp, Ether, ARP, conf
from colorama import Fore, Style

class ARPScanner:
    def __init__(self, interface, ips):
        self.interface = interface
        self.ips = ips

    def scan(self):
        print(Fore.YELLOW + "[*] Scanning..." + Style.RESET_ALL) 
        start_time = datetime.now()

        conf.verb = 0 
        ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=self.ips), 
                         timeout=2, 
                         iface=self.interface,
                         inter=0.1)

        print(Fore.GREEN + "\n[*] IP - MAC" + Style.RESET_ALL) 
        for snd, rcv in ans: 
            print(Fore.CYAN + rcv.sprintf(r"%ARP.psrc% - %Ether.src%") + Style.RESET_ALL)
        
        stop_time = datetime.now()
        total_time = stop_time - start_time 
        print(Fore.YELLOW + "\n[*] Scan Complete. Duration: " + str(total_time) + Style.RESET_ALL)

def main():
    parser = argparse.ArgumentParser(description="ARP Scanner")
    parser.add_argument("interface", help="Network interface to use")
    parser.add_argument("ips", help="IP range to scan (e.g., 192.168.1.0/24)")
    
    args = parser.parse_args()
    
    scanner = ARPScanner(args.interface, args.ips)
    scanner.scan()

if __name__ == "__main__":
    main()
