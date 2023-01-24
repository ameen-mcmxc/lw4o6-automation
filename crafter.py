#!/usr/bin/env python3

from scapy.all import *
import random

nat44_ip="203.0.133.1"


def packet_callback(packet):
    if packet.haslayer(Ether) and packet.haslayer(IPv6) and packet.haslayer(IP) and packet.haslayer(ICMP) and packet.haslayer(Raw) and packet[IP].src == nat44_ip:
        # Extract the ICMP.id value from the found packet
        icmp_id = packet[ICMP].id
        # Generate random value for ICMP.seq
        icmp_seq = random.randint(1, 65535)
        # Craft a new packet
        new_packet = (Ether(src="00:0c:29:82:0d:ac", dst="00:0c:29:18:4c:dc") /
                      IPv6(dst="2001:db8:2::2",src="2001:db8:0:1::2") /
                      IP(src=nat44_ip, dst="192.0.2.2") /
                      ICMP(id=icmp_id,seq=icmp_seq) /
                      Raw(load="From Ameen with Love"))
        sendp(new_packet,iface="ens34")

# Sniff packets on interface ens34
sniff(iface="ens34", prn=packet_callback)
