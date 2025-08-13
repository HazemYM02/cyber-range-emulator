#!/bin/bash
# Simple Wapiti scan example
TARGET="$1"

if [ -z "$TARGET" ]; then
    echo "Usage: $0 <target_url>"
    exit 1
fi

wapiti -u "$TARGET" -f html -o /opt/tools/wapiti-report.html
echo "Scan complete. Report saved to /opt/tools/wapiti-report.html"
