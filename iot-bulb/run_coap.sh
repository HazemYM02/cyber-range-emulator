#!/bin/sh
# Minimal CoAP device using libcoap example server as a stub.
# You can interact with it using coap-client on port 5683/udp.
coap-server -v 3 -d 4 -A 0.0.0.0 -p 5683 &
SERVER_PID=$!

# keep running
while true; do sleep 3600; done
wait $SERVER_PID
