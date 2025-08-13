#!/bin/bash

# Enable IP forwarding
echo 1 > /proc/sys/net/ipv4/ip_forward

# Configure routing for directly connected subnets
ip route add 10.88.10.0/24 dev eth0
ip route add 10.88.20.0/24 dev eth1
ip route add 10.88.40.0/24 dev eth2
ip route add 10.88.30.0/24 via 10.88.40.10

# Keep container alive
sleep infinity