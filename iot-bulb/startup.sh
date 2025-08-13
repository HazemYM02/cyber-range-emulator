#!/bin/sh
set -e
ip route replace default via 10.88.20.254

nohup /opt/run_coap.sh >/opt/coap.log 2>&1 &

sleep infinity
