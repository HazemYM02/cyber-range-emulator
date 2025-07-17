#!/bin/bash

# Add route to reach victims via router (assumes router is 172.20.0.1)
# Enable IP forwarding
echo 1 > /proc/sys/net/ipv4/ip_forward

# Optional: show routing table
ip route add 172.21.0.0/24 via 172.20.0.1
ip route add 172.22.0.0/24 via 172.20.0.1

# NAT
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

# Keep container running
sleep infinity


# Keep container alive
exec "$@"