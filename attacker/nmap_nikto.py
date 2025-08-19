import subprocess
import xml.etree.ElementTree as ET
from datetime import datetime
import threading
import os
import random
import re
import logging

# === Configuration ===
TARGET_IPS = [
    "10.88.30.10",  # Victim node
    "10.88.20.10",  # IoT device 1
    "10.88.20.12",  # IoT device 2
    "10.88.20.13",  # IoT device 3
    "10.88.20.14",  # IoT device 4
]

# Use absolute paths inside container
LOG_DIR = "/app/logs"
NIKTO_OUTPUT_DIR = "/app/nikto_results"

# Ensure directories exist
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(NIKTO_OUTPUT_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, f"pentest_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

NMAP_TIMEOUT = 600  # seconds
NIKTO_TIMEOUT = 600  # seconds

# === Setup logging ===
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log(message, level="info"):
    getattr(logging, level)(message)
    print(message)

# === Helper Functions ===
def is_host_up(ip):
    try:
        subprocess.run(["ping", "-c", "1", ip], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        log(f"[-] Host {ip} is unreachable.", "warning")
        return False

def run_nmap_scan(target_ip):
    log(f"[*] Scanning {target_ip} with Nmap...")
    nmap_output_path = os.path.join(LOG_DIR, f"nmap_{target_ip}.xml")
    nmap_command = [
        "nmap", "-sV", "--script=vulners", "-p-", "-T4", "-Pn",
        "-oX", nmap_output_path, target_ip
    ]
    try:
        subprocess.run(nmap_command, check=True, capture_output=True, text=True, timeout=NMAP_TIMEOUT)
        log(f"[+] Nmap scan for {target_ip} completed. Output saved to {nmap_output_path}")
        return True
    except subprocess.TimeoutExpired:
        log(f"[-] Nmap scan timed out for {target_ip}.", "error")
        return False
    except subprocess.CalledProcessError as e:
        log(f"[-] Nmap scan for {target_ip} failed: {e.stderr}", "error")
        return False

def parse_nmap_results(target_ip):
    """Extract HTTP/HTTPS ports and CVE severity data."""
    http_ports = []
    severity_count = {"Critical": 0, "High": 0, "Medium": 0, "Low": 0}
    cvss_pattern = re.compile(r"CVSS:([0-9]+\.[0-9]+)")

    nmap_output_path = os.path.join(LOG_DIR, f"nmap_{target_ip}.xml")

    try:
        tree = ET.parse(nmap_output_path)
        root = tree.getroot()

        # Check if host is up
        status = root.find("host/status")
        if status is not None and status.get("state") != "up":
            log(f"[-] Host {target_ip} is down according to Nmap results.", "warning")
            return []

        for port in root.findall("host/ports/port"):
            portid = port.get("portid")
            service = port.find("service")
            scripts = port.findall("script")

            if service is not None:
                service_name = service.get("name", "").lower()
                # Detect HTTP or HTTPS services
                if service_name in ["http", "https"]:
                    http_ports.append((portid, service_name == "https"))

            for script in scripts:
                if script.get("id") == "vulners":
                    output = script.get("output", "")
                    for line in output.splitlines():
                        match = cvss_pattern.search(line)
                        if match:
                            try:
                                score = float(match.group(1))
                                if score >= 9.0:
                                    severity_count["Critical"] += 1
                                elif score >= 7.0:
                                    severity_count["High"] += 1
                                elif score >= 4.0:
                                    severity_count["Medium"] += 1
                                else:
                                    severity_count["Low"] += 1
                            except ValueError:
                                continue

        log(f"[+] [{target_ip}] Vulnerability summary: {severity_count}")
        return http_ports
    except Exception as e:
        log(f"[-] Failed to parse Nmap results for {target_ip}: {e}", "error")
        return []

def run_nikto_scan(target_ip, port, use_ssl=False):
    protocol = "https" if use_ssl else "http"
    output_path = os.path.join(NIKTO_OUTPUT_DIR, f"nikto_{target_ip}_{port}.txt")
    nikto_command = [
        "nikto", "-h", f"{protocol}://{target_ip}:{port}",
        "-o", output_path, "-Format", "txt"
    ]
    log(f"[*] Running Nikto scan on {protocol}://{target_ip}:{port}...")
    try:
        subprocess.run(nikto_command, check=True, capture_output=True, text=True, timeout=NIKTO_TIMEOUT)
        log(f"[+] Nikto scan completed for {target_ip}:{port}. Output saved to {output_path}")
        return True
    except subprocess.TimeoutExpired:
        log(f"[-] Nikto scan timed out for {target_ip}:{port}.", "error")
        return False
    except subprocess.CalledProcessError as e:
        log(f"[-] Nikto scan failed for {target_ip}:{port}: {e.stderr}", "error")
        return False

def attack_target(target_ip):
    log(f"\n[=== Targeting {target_ip} ===]")
    log(f"Current working directory: {os.getcwd()}")
    log(f"Log file path: {LOG_FILE}")

    if not is_host_up(target_ip):
        return

    if not run_nmap_scan(target_ip):
        return

    http_ports = parse_nmap_results(target_ip)
    if not http_ports:
        log(f"[-] No HTTP/HTTPS ports found on {target_ip}.")
        return

    ports_str = ", ".join([f"{port}{' (HTTPS)' if ssl else ''}" for port, ssl in http_ports])
    log(f"[+] [{target_ip}] Discovered HTTP/HTTPS ports: {ports_str}")

    for port, use_ssl in http_ports:
        run_nikto_scan(target_ip, port, use_ssl)

# === Main Entry Point ===
if __name__ == "__main__":
    log("[*] Starting Nmap+Nikto randomized pentest.")
    log(f"[*] Available Targets: {', '.join(TARGET_IPS)}")

    selected_target = random.choice(TARGET_IPS)
    log(f"[*] Randomly selected target: {selected_target}")

    attack_thread = threading.Thread(target=attack_target, args=(selected_target,))
    attack_thread.start()
    attack_thread.join()

    log("[+] Test completed. Check logs and Nikto reports.")
