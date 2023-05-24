#!/usr/bin/env python3

# This script is used to send TCP packet from the client to the Server.
# However, it adds an extra layer of security by encrypting the payload of the TCP packet.

from scapy.all import *

from cryptography.fernet import Fernet

# create a Fernet key for encryption
key = Fernet.generate_key()
fernet = Fernet(key)

# plaintext TCP payload
plaintext = b"I am the payload of TCP packet"

# encrypt the payload
encrypted_payload = fernet.encrypt(plaintext)



ip = IP(dst="192.0.2.2")
tcp = TCP(dport=80)
pkt = ip/tcp/encrypted_payload

send(pkt)
