#!/usr/bin/env python3

from scapy.all import *



# This scritp sniffes the communication channel on Interface ens34, looks UDP traffic
# Then, it spoofes the source IP address of the found packet and sends identical packet to the same recipient.

# function to process the packet
def process_packet(packet):
    # check if the packet is a UDP packet
    if packet.haslayer(UDP):
        # extract the source port
        src_port = packet[UDP].sport
        print("[+] Found UDP packet with source port: ", src_port)
        # craft a new UDP packet
        ip = IPv6(dst="2001:db8:2::2",src="2001:db8:0:1::2")
        eth= Ether(src="00:0e:31:29:5b:af")
        udp = UDP(sport=src_port, dport=80)
        data = "From Ameen with Love!"
        packet = eth/ip/udp/data
        sendp(packet, iface='ens34',return_packets=True)


# start sniffing on ens34
sniff(iface='ens34', prn=process_packet)
