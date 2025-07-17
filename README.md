# Cyber-Range Emulator

A modular, Docker-based cybersecurity training and testing environment designed to simulate real-world cyber operations in both flat and segmented networks. Originally built around a flat Docker bridge network, the environment has evolved to support isolated subnets, firewalls, IoT nodes, and centralized log collection.

---

## Project Goals

- Quick-start, modular lab setup for penetration testing and network defense training  
- Simulate common attack paths and misconfigurations in controlled networks  
- Launch security tools like Nmap, Snort, DVWA, and more  
- Monitor attacks and logs using centralized Splunk integration  
- Visualize container roles and connectivity through a custom interactive GUI  
- Practice red teaming, packet analysis, and basic log correlation

---

## Technologies Used

- **Docker + Docker Compose** — containerized lab topology  
- **Python** — for orchestration and visualization  
- **Streamlit + PyVis** — network visualization GUI  
- **DVWA** — Damn Vulnerable Web App targets  
- **Snort, tcpdump, netcat, Nmap** — penetration and detection tools  
- **Splunk** — centralized log collection and analysis  
- **Bash, iptables, iproute2** — firewall rule testing and network manipulation

---

## Network Topology Overview

### Core Nodes

| Container    | Role                       | Notes                          |
|--------------|----------------------------|--------------------------------|
| `attacker`   | Pentesting tools           | Can reach all targets          |
| `router`     | Central switch/router node | Connects multiple subnets      |
| `firewall`   | Core firewall              | Simulates packet filtering     |
| `victim`     | DVWA instance              | Accessible at port 8081        |
| `victim1`    | DVWA instance              | Accessible at port 8082        |
| `victim2`    | DVWA instance              | Accessible at port 8083        |
| `splunk`     | Log monitoring server      | Accessible at port 18000       |

### Home Network Extension

| Container        | Role                  | IP Range          |
|------------------|-----------------------|-------------------|
| `home_router`     | Home Wi-Fi router      | 172.30.100.254     |
| `home_firewall`   | Home network firewall  | Intercepts traffic |
| `smart_tv`        | IoT device             | 172.30.100.10      |
| `smart_light`     | IoT device             | 172.30.100.11      |
| `laptop`          | User endpoint          | 172.30.100.20      |

This network is isolated via custom bridges and connected to the main router via a dedicated firewall (`home_firewall`), with packet logging and inspection enabled.

---

## Key Features and Additions

- DVWA web applications deployed on multiple victim nodes for web pentesting  
- Attacker node with tools: `nmap`, `sqlmap`, `hydra`, `john`, `wfuzz`, and more  
- Firewall rules on `firewall` and `home_firewall` simulate real-world ACLs and packet drops  
- Splunk container listens on port 514 for forwarded syslog messages and displays logs in a web UI  
- Real-time packet inspection and log forwarding using `rsyslog` and `iptables`  
- Visual GUI with shape-based node roles:  
  - Router: star  
  - Firewalls: box  
  - Endpoints/IoT: ellipse  
  - Splunk: hexagon

---

## Getting the Cyber-Range Emulator Up and Running

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

# 5. Access a container to interact with tools
docker exec -it attacker bash

# 6. Launch the network visualizer (Streamlit GUI)
streamlit run network_gui.py

# 7. Access Splunk (for logs)
http://localhost:8000
