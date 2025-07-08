# Cyber-Range Emulator

A modular, Docker-based cybersecurity training and testing environment designed to simulate real-world cyber operations in a **flat network**. This simplified topology runs all containers on a single shared Docker bridge network — ideal for quick prototyping, instruction, and testing without complex routing.

---

## 🚀 Project Goals

- ⚡ **Quick-start, single-network design**
- 🎯 Ideal for labs, workshops, and beginner training
- 🧰 Launch common security tools like Nmap, Snort, DVWA
- 📡 Observe and test attacks across all machines freely
- 🖼️ Visualize container roles and communication paths via a custom GUI
- 🔍 Use `tcpdump`, `ping`, `curl`, `nmap` to test connectivity and visibility

---

## 🧰 Technologies Used

- **Docker + Docker Compose** — containerized environment
- **Python** — with Docker SDK, Streamlit, and PyVis
- **DVWA** — Damn Vulnerable Web App
- **tcpdump**, **Netcat**, **Nmap**, **Snort** — tools for testing and detection
- **Streamlit + PyVis** — interactive network visualization
- **Bash & iproute2** — basic container networking setup

---

## 🔄 Flat Network Topology

All containers live on the **default Docker bridge network**. No separate subnetting, routing, or custom bridges.

| Container    | Role                  | Notes                        |
|--------------|-----------------------|------------------------------|
| `attacker`   | Offensive tools, Nmap | Can reach all other nodes   |
| `router`     | Simulated gateway     | Optional routing behavior   |
| `firewall`   | Packet filtering test | Hosts iptables rules        |
| `victim`     | DVWA web target       | Accessible via port 8081    |
| `victim1`    | Extra DVWA instance   | Accessible via port 8082    |
| `victim2`    | Extra DVWA instance   | Accessible via port 8083    |

---

## Getting the Cyber-Range Emulator Up and Running

Follow these steps to launch the full emulator environment with all nodes:

```bash
# 1. Clone the repository
git clone https://github.com/HazemYM02/cyber-range-emulator.git
cd cyber-range-emulator

# 2. Build all Docker containers
docker compose build

# 3. Start the entire lab environment in the background
docker compose up -d

# 4. Confirm all containers are running
docker ps

# 5. (Optional) Access a container to interact with tools
docker exec -it attacker bash

# 6. Launch the network visualizer in your browser
streamlit run network_gui.py
