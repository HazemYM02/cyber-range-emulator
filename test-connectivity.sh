#!/bin/bash

set -e

declare -A NODES=(
  [attacker]=10.88.10.10
  [router]=10.88.10.254
  [iot1]=10.88.20.10
  [victim]=10.88.30.10
  [firewall]=10.88.40.10
)

# Test connectivity from one container to another and trace the path
test_connection() {
  local FROM=$1
  local TO=$2
  local TO_IP=${NODES[$TO]}
  echo -n "[$FROM → $TO] "

  # Ping test
  docker exec "$FROM" ping -c 1 -W 1 "$TO_IP" &> /dev/null
  if [ $? -ne 0 ]; then
    echo "❌ Unreachable"
    return
  fi

  # Traceroute check
  TRACE=$(docker exec "$FROM" traceroute -n -m 3 "$TO_IP" 2>/dev/null | tail -n +2 | awk '{print $2}')
  if [ "$FROM" = "attacker" ] && [ "$TO" = "iot1" ]; then
    if [[ "$TRACE" == *"10.88.10.254"* && "$TRACE" == *"10.88.20.10"* ]]; then
      echo "✅ via router"
    else
      echo "❌ bypassed router"
    fi
  elif [ "$FROM" = "attacker" ] && [ "$TO" = "victim" ]; then
    if [[ "$TRACE" == *"10.88.10.254"* && "$TRACE" == *"10.88.40.10"* && "$TRACE" == *"10.88.30.10"* ]]; then
      echo "✅ via router+firewall"
    else
      echo "❌ incorrect path"
    fi
  else
    echo "✅ reachable"
  fi
}

# Ensure traceroute is installed in each container
for c in attacker victim iot1 router firewall; do
  docker exec "$c" bash -c "command -v traceroute || apt update && apt install -y traceroute"
done

echo "🔍 Testing network routing paths..."

# Run specific important path tests
test_connection attacker iot1
test_connection attacker victim
test_connection iot1 attacker
test_connection victim attacker
test_connection victim iot1

echo "✅ Done"
