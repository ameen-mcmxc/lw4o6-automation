#!/bin/bash

# Flushing iptbales rules
iptables -F
iptables -X
ip6tables -F
ip6tables -X

# enable IPv4 & IPv6 forwarding
echo 1 > /proc/sys/net/ipv4/ip_forward
echo 1 > /proc/sys/net/ipv6/conf/all/forwarding


B4V6ADDR='2001:db8:0:1::2/64'
B4V6ADDR2='2001:db8:0:1::2' # This is just same IP but without prefix
B4V4ADDR='203.0.113.1'
B4INT='ens35'
AFTRV6ADDR='2001:db8:2::2'
V6NEXTHOP='2001:db8:0:1::1'
target='192.0.2.0/24'
ports_range='1024-2047'
tun_int='lw4o6-tun'

ip link set $B4INT up
ip -6 addr add $B4V6ADDR dev $B4INT
ip -6 tunnel add lw4o6-tun remote $AFTRV6ADDR local $B4V6ADDR2 mode ipip6 encaplimit 4 hoplimit 64 tclass 0x00 flowlabel 0x00000
ip link set dev $tun_int mtu 1400 up
ip addr add $B4V4ADDR/32 dev $tun_int nodad

ip route add $target dev $tun_int proto static
ip -6 route add 2001:db8:2::/64 via $V6NEXTHOP dev $B4INT src $B4V6ADDR2

# SNAT Section
iptables -t nat --flush
iptables -t nat -A POSTROUTING -p tcp  -o $tun_int -j SNAT --to-source $B4V4ADDR:$ports_range
iptables -t nat -A POSTROUTING -p udp  -o $tun_int -j SNAT --to-source $B4V4ADDR:$ports_range
iptables -t nat -A POSTROUTING -p icmp -o $tun_int -j SNAT --to-source $B4V4ADDR:$ports_range

# To allow DNS queries
iptables -A OUTPUT -p udp -m udp --dport 53 -j ACCEPT
