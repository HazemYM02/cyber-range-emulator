#!/bin/bash

# Enable IP forwarding
sysctl -w net.ipv4.ip_forward=1
iptables -P FORWARD ACCEPT

# Show routing table (optional)
echo "[home_router] Routing table:"
ip route

# Keep container alive
exec "$@"
