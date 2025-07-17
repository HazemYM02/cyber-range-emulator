#!/bin/bash

# Optional: enable job control
set -m

# Add static route to victim network via router
ip route add 172.21.0.0/24 via 172.20.0.254

# Display routing table for debugging
ip route

# Keep container running
sleep infinity