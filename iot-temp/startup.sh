#!/bin/sh
set -e
ip route replace default via 10.88.20.254

: "${MQTT_BROKER:=10.88.20.200}"
: "${MQTT_TOPIC:=home/iot/temp}"
: "${PUBLISH_EVERY:=5}"

nohup sh -c "while true; do python3 /opt/publish_temp.py \"$MQTT_BROKER\" \"$MQTT_TOPIC\"; sleep $PUBLISH_EVERY; done" >/opt/mqtt.log 2>&1 &

sleep infinity
