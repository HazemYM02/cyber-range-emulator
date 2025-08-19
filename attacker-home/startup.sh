#!/bin/bash
set -e
echo 1 > /proc/sys/net/ipv4/ip_forward
ip -4 addr show
exec bash