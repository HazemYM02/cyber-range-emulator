import subprocess
import xml.etree.ElementTree as ET
from datetime import datetime
import threading
import os

# Config
TARGET_IPS = ["172.21.0.2", "172.21.0.3", "172.21.0.4"]  # Replace with your targets
LOG_FILE = f"pentest_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"  # Fixed: Removed forward slashes
NIKTO_OUTPUT_DIR = "nikto_results"

def log(message):
    """Print and log messages."""
    print(message)
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()}: {message}\n")

def run_nmap_scan(target_ip):
    """Run Nmap scan on a target IP."""
    log(f"[*] Scanning {target_ip}...")
    nmap_command = [
        "nmap",
        "-sV",                              # Service version detection
        "--script=vulners",                 # CVE detection
        "-p-",                              # Scan all ports
        "-T4",                              # Aggressive timing
        "-oX", f"nmap_{target_ip}.xml",    # Output XML per target
        target_ip
    ]
    try:
        subprocess.run(nmap_command, check=True, capture_output=True, text=True)
        log(f"[+] Nmap scan for {target_ip} completed.")
        return True
    except subprocess.CalledProcessError as e:
        log(f"[-] Nmap scan for {target_ip} failed: {e.stderr}")
        return False

def parse_nmap_results(target_ip):
    """Parse Nmap XML results for HTTP/HTTPS services."""
    http_ports = []
    try:
        tree = ET.parse(f"nmap_{target_ip}.xml")
        root = tree.getroot()

        for host in root.findall("host"):
            for port in host.findall("ports/port"):
                service = port.find("service")
                if service is not None and service.get("name") in ["http", "https"]:
                    http_ports.append(port.get("portid"))

        return http_ports
    except Exception as e:
        log(f"[-] Error parsing Nmap results for {target_ip}: {e}")
        return []

def run_nikto_scan(target_ip, port):
    """Run Nikto scan on a target IP and port."""
    log(f"[*] [{target_ip}] Testing web vulnerabilities on port {port}...")
    nikto_command = [
        "nikto",
        "-h", f"http://{target_ip}:{port}",  # Use 'https://' if TLS is detected
        "-o", f"{NIKTO_OUTPUT_DIR}/nikto_{target_ip}_{port}.txt",
        "-Format", "txt"
    ]
    try:
        subprocess.run(nikto_command, check=True, capture_output=True, text=True)
        log(f"[+] Nikto scan for {target_ip}:{port} completed.")
        return True
    except subprocess.CalledProcessError as e:
        log(f"[-] Nikto scan for {target_ip}:{port} failed: {e.stderr}")
        return False

def attack_target(target_ip):
    """Full attack workflow for a single target."""
    log(f"\n[=== Targeting {target_ip} ===]")
    if not run_nmap_scan(target_ip):
        return

    http_ports = parse_nmap_results(target_ip)
    if not http_ports:
        log(f"[-] No HTTP/HTTPS services found on {target_ip}.")
        return

    log(f"[+] [{target_ip}] Found HTTP/HTTPS ports: {', '.join(http_ports)}")
    for port in http_ports:
        run_nikto_scan(target_ip, port)

if __name__ == "__main__":
    # Create output directory
    os.makedirs(NIKTO_OUTPUT_DIR, exist_ok=True)

    # Initialize log file
    with open(LOG_FILE, "w") as f:
        f.write(f"Automated Penetration Test - {datetime.now()}\n")

    log("[*] Starting AUTOMATED PENETRATION TEST (Nmap + Nikto)...")
    log(f"[*] Targets: {', '.join(TARGET_IPS)}")
    log("[*] Note: Authorized test. Using Nmap for scanning and Nikto for web exploitation.")

    # Run attacks in parallel threads
    threads = []
    for ip in TARGET_IPS:
        thread = threading.Thread(target=attack_target, args=(ip,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    log("[+] Automated penetration test completed. Review logs and results.")
