import time
from datetime import datetime

LOG_FILE_PATH = "/var/log/kern.log"  # Change to /var/log/syslog if kern.log is empty
ALERT_OUTPUT_FILE = "/opt/alerts.txt"
KEYWORDS = ["NIKTO_SCAN", "NMAP_SCAN", "POSSIBLE_SCAN"]

def tail(filepath):
    with open(filepath, "r") as f:
        f.seek(0, 2)  # Go to end of file
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.5)
                continue
            yield line

def log_alert(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_message = f"[{timestamp}] ALERT: {message}"
    print(full_message)
    with open(ALERT_OUTPUT_FILE, "a") as out:
        out.write(full_message + "\n")

# Monitor logs and capture alerts
for line in tail(LOG_FILE_PATH):
    if any(keyword in line for keyword in KEYWORDS):
        log_alert(line.strip())