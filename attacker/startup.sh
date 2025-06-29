#!/bin/bash
ip route add 172.29.0.0/24 via 172.28.0.254
ip route add 172.30.0.0/24 via 172.28.0.254
exec "$@"
