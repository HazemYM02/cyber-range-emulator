#!/bin/sh

echo 1 > /proc/sys/net/ipv4/ip_forward
ip route replace default via 172.24.0.1

# Flush existing rules
iptables -F
iptables -t nat -F

# Default: DROP all forwarding unless allowed
iptables -P FORWARD DROP

# Allow established traffic to flow
iptables -A FORWARD -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# Allow HTTP (port 80) from dmz (eth0) to home network (eth1)
iptables -A FORWARD -i eth0 -o eth1 -p tcp --dport 80 -j ACCEPT

# Allow DNS if needed
iptables -A FORWARD -i eth0 -o eth1 -p udp --dport 53 -j ACCEPT

# Allow internal traffic from home network to router/dmz (optional)
iptables -A FORWARD -i eth1 -o eth0 -j ACCEPT

# NAT for returning packets
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

# Log and drop all other inbound traffic to home_network
iptables -A FORWARD -i eth0 -o eth1 -j LOG --log-prefix "HOMEFW DROP: "
iptables -A FORWARD -i eth0 -o eth1 -j DROP

# Start logging service
service rsyslog start

# Keep container running
exec sleep infinity
