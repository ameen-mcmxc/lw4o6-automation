#!/bin/bash

# Flush existing iptables rules
iptables -F

# Set default policies
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

# Allow established connections
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Allow loopback interface
iptables -A INPUT -i lo -j ACCEPT

# Rule 1: Discard DNS query packets
iptables -A INPUT -p udp --dport 53 -j DROP

# Rule 2: Permit DNS query packets at a rate of 10 packets per second
iptables -A INPUT -p udp --dport 53 -m limit --limit 100/s --limit-burst 200 -j ACCEPT

# Save the iptables configuration
iptables-save > /etc/iptables/rules.v4

# Restart the networking service (may vary based on your Linux distribution)
service networking restart
