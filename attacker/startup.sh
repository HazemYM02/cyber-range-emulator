#!/bin/bash
# Add routes if attacker needs to reach victims
ip route add 192.168.102.0/24 via 192.168.100.1
exec "$@"