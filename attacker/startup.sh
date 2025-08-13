#!/bin/sh
ip route replace default via 10.88.10.254
ip route add 10.88.20.0/24 via 10.88.10.254
ip route add 10.88.30.0/24 via 10.88.10.254

sleep infinity