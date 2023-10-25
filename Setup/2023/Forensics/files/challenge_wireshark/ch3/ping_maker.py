from scapy.all import IP, ICMP, send
from scapy.sendrecv import sr

for i in "CSC{custom_icmp_packets_lol}":
    p = IP(dst='192.168.205.109')/ICMP(id=ord(i))
    sr(p)

# Idea on making custom ICMP packets taken from:
# https://stackoverflow.com/questions/23269226/scapy-in-a-script