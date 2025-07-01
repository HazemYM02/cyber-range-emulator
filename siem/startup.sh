#!/bin/bash

# Optional: forward to Splunk HEC or syslog server
# echo "*.* @172.30.0.80:514" >> /etc/rsyslog.conf

# Start IP forwarding if needed
sysctl -w net.ipv4.ip_forward=1

# Print container IP info for visibility
ip a

# Run the default command
exec "$@"
