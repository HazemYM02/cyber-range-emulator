#!/bin/bash
ip route add 172.20.0.0/24 via 172.21.0.254
apache2ctl -D FOREGROUND
exec "$@"