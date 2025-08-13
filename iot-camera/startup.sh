#!/bin/sh
set -e
ip route replace default via 10.88.20.254

nohup python3 /opt/camera.py >/opt/camera.log 2>&1 &

sleep infinity
