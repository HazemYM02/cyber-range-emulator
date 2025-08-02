#!/bin/sh

ip route replace default via 172.25.0.1

# Keep alive
exec sleep infinity