#!/bin/bash
# Enable IP forwarding
echo 1 > /proc/sys/net/ipv4/ip_forward
# NAT
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

# Keep container running
sleep infinity

# Keep container alive
exec "$@"