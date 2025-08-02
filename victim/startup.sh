#!/bin/sh

# Set default route to firewall
ip route replace default via 172.21.0.1
apache2ctl -D FOREGROUND

# Keep container alive
exec tail -f /dev/null
exec "$@"