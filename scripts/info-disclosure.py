#!/usr/bin/env python3

# This script prints out the payload content of the sniffed UDP or TCP
# It also prints out the content of the embedded data in the ICMPv6 Echo request

from scapy.all import *

def packet_handler(packet):
        if UDP in packet:
            udp_payload = packet[UDP].payload
            print(f"Payload: {udp_payload}")
        elif ICMPv6EchoRequest in packet:
            icmp6_payload = packet[ICMPv6EchoRequest].data
            print(f"ICMPv6 echo request embedded Data: {icmp6_payload}")
        elif TCP in packet and packet[IPv6].src == "2001:db8:0:1::2":
            tcp_payload = packet[TCP].payload
            print(f"TCP Payload: {tcp_payload}")
sniff(iface='ens34', filter='udp or icmp6 or tcp', prn=packet_handler)
