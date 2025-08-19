#!/usr/bin/env python3

import subprocess
import os

# Define the target IPs
VICTIM_NODE = "10.88.30.10"
IOT_DEVICES = ["10.88.20.10", "10.88.20.12", "10.88.20.13", "10.88.20.14"]

# Output directory for scan results
OUTPUT_DIR = "./wapiti_scan_results"

def run_wapiti_scan(target):
    """Run a Wapiti scan on the target and save results to an HTML file."""
    output_file = os.path.join(OUTPUT_DIR, f"wapiti_scan_{target.replace('.', '_')}.html")
    
    print(f"[+] Scanning {target}...")
    try:
        subprocess.run(
            ["wapiti", "-u", f"http://{target}/", "-f", "html", "-o", output_file],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        print(f"[+] Scan completed for {target}. Results saved to: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"[-] Error scanning {target}: {e.stderr.decode().strip()}")
    except FileNotFoundError:
        print("[-] Wapiti is not installed or not in PATH. Install it with: pip install wapiti3")

def main():
    # Create output directory if it doesn't exist
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Scan the victim node
    run_wapiti_scan(VICTIM_NODE)

    # Scan each IoT device
    for device in IOT_DEVICES:
        run_wapiti_scan(device)

    print(f"\n[+] All scans completed. Results saved in: {os.path.abspath(OUTPUT_DIR)}")

if __name__ == "__main__":
    main()
