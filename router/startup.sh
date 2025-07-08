#!/bin/bash

# Add route to reach victims via router (assumes router is 172.20.0.1)
ip route add 172.21.0.0/24 via 172.20.0.1
ip route add 172.22.0.0/24 via 172.20.0.1

# Optional: logging message
echo "[attacker] Routes to firewall and internal net added via router."

# Keep container alive
exec "$@"