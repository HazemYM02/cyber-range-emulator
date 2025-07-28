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

# Automation Prevention
iptables -A INPUT -p tcp --dport 80 -m string --string "Nikto" --algo bm -j LOG --log-prefix "NIKTO_SCAN "
iptables -A INPUT -p tcp --dport 80 -m string --string "nmap" --algo bm -j LOG --log-prefix "NMAP_SCAN "

# Start rsyslog for logging
service rsyslog start

# Enable kernel logging for iptables
modprobe ipt_LOG
service rsyslog start

# Start monitor
python3 /opt/monitor.py &

# Keep alive
exec sleep infinity