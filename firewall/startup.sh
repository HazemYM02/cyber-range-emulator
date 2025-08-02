#!/bin/sh

echo 1 > /proc/sys/net/ipv4/ip_forward
ip route replace default via 172.20.0.1

# Optional: flush and log iptables rules
iptables -F
iptables -t nat -F
iptables -A FORWARD -i eth0 -o eth1 -j ACCEPT
iptables -A FORWARD -i eth1 -o eth0 -j ACCEPT
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

# Start logging service if needed
service rsyslog start 2>/dev/null

# Keep alive
exec sleep infinity