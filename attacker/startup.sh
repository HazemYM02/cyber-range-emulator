#!/bin/bash
echo "[+] Starting up..."
sysctl -w net.ipv4.ip_forward=1

# Add route to home network via router
ip route add 172.30.100.0/24 via 172.30.100.254

sleep infinity