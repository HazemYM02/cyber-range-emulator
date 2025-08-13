#!/bin/bash

# Set default route via firewall
ip route replace default via 10.88.30.253

# Start Apache properly
apache2ctl -D FOREGROUND