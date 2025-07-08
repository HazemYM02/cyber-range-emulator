#!/bin/bash

# Enable IP forwarding
sysctl -w net.ipv4.ip_forward=1

# Flush any existing firewall rules
iptables -F

# Default policy: DROP everything (you can make it ACCEPT for testing)
iptables -P FORWARD DROP

# Allow traffic from internal to router and back (stateful)
iptables -A FORWARD -s 172.22.0.0/24 -d 172.20.0.0/16 -m state --state NEW,ESTABLISHED,RELATED -j ACCEPT
iptables -A FORWARD -s 172.20.0.0/16 -d 172.22.0.0/24 -m state --state ESTABLISHED,RELATED -j ACCEPT

# Optional: Log accepted traffic (comment out if noisy)
# iptables -A FORWARD -j LOG --log-prefix "FW-LOG: " --log-level 4

echo "[firewall] IP forwarding enabled and firewall rules set."

exec "$@"