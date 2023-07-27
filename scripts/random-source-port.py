#!/usr/bin/env python3

from scapy.all import *



# This script sniffs the communication channel on Interface ens34, looks for UDP traffic
# Then, it spoofs the source IP address of the found packet and sends an identical packet to the same recipient.
# However, it sends the wrong source port number.

# function to process the packet
def process_packet(packet):
    # check if the packet is a UDP packet
    if packet.haslayer(UDP):
        print("[+] Found UDP packet with source port: ", src_port)
        # craft a new UDP packet
        src_port = RandShort()
        ip = IPv6(dst="2001:db8:2::2",src="2001:db8:0:1::2")
        eth= Ether(src="00:0e:31:29:5b:af")
        udp = UDP(sport=src_port, dport=80)
        data = "From Ameen with Love!"
        packet = eth/ip/udp/data
        sendp(packet, iface='ens34',return_packets=True)


# start sniffing on ens34
sniff(iface='ens34', filter="udp", prn=process_packet)
