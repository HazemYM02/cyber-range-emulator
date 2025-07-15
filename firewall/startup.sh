#!/bin/bash

# Enable IP forwarding
echo 1 > /proc/sys/net/ipv4/ip_forward

# Clear rules
iptables -F
iptables -t nat -F

# Basic forwarding + NAT
iptables -A FORWARD -i eth0 -o eth1 -j ACCEPT
iptables -A FORWARD -i eth1 -o eth0 -j ACCEPT
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

# Log all dropped packets
iptables -A FORWARD -j LOG --log-prefix "FIREWALL DROP: " --log-level 4

# Start rsyslog for logging
service rsyslog start

# Keep alive
exec sleep infinity