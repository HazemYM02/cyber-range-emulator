#!/bin/sh

# Enable IP forwarding
echo 1 > /proc/sys/net/ipv4/ip_forward

# Start Cockpit
/usr/lib/cockpit/cockpit-ws --no-tls &

# Enable UFW
ufw --force enable
ufw logging on
ufw default deny incoming
ufw allow out on eth0

# Start Snort in the background, log in fast mode
snort -i any -c /etc/snort/snort.conf -A fast -l /var/log/snort &

# Stream Snort logs to Splunk over TCP 9997
tail -F /var/log/snort/fast.log | nc -q 1 10.88.10.200 9997 &

ip route replace default via 10.88.40.254

sleep infinity