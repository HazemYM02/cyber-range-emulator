# Cyber-Range Emulator

A modular, Docker-based cybersecurity training and testing environment designed to simulate real-world cyber operations in both flat and segmented networks. Originally built around a flat Docker bridge network, the environment has evolved to support **multiple isolated subnets, dedicated firewalls, IoT devices, and centralized log collection**.

---

## Project Goals

- Quick-start, modular lab setup for penetration testing and network defense training  
- Simulate common attack paths and misconfigurations in controlled networks  
- Launch security tools like Nmap, Nikto, Wapiti, ZAP, and more  
- Monitor attacks and logs using centralized Splunk integration  
- Visualize container roles and connectivity through a custom interactive GUI  
- Practice red teaming, packet analysis, ARP spoofing, and basic log correlation

---

## Technologies Used

- **Docker + Docker Compose** — containerized lab topology  
- **Python** — for orchestration and visualization  
- **Streamlit + PyVis** — network visualization GUI  
- **DVWA** — Damn Vulnerable Web App targets  
- **ZAP CLI, Wapiti, Nikto, Nmap** — penetration and scanning tools  
- **Splunk** — centralized log collection and analysis  
- **Bash, iptables, iproute2** — firewall rule testing and network manipulation

---

## Network Topology Overview

### Core Nodes

| Container           | Role                       | Notes / Access Ports         |
|---------------------|----------------------------|------------------------------|
| `attacker`          | Pentesting tools           | Nmap, Nikto, Wapiti, ZAP CLI |
| `router`            | Central router/switch      | Connects all subnets         |
| `firewall`          | Core firewall              | Cockpit web UI: **9090**     |
| `victim`            | DVWA target                | **http://localhost:8000**    |
| `iot1`              | IoT device                 | Test for IoT exploits        |
| `iot-bulb`          | IoT smart bulb             | Simulated vulnerable device  |
| `iot-camera`        | IoT camera                 | Accessible at **8081**       |
| `iot-thermostat-web`| IoT thermostat web panel   | Accessible at **8082**       |
| `splunk`            | Log monitoring server      | **http://localhost:8001**    |

---

## Key Features and Additions

- **Multiple IoT nodes** to simulate diverse attack surfaces  
- **Attacker node** preloaded with scanning and exploitation tools: `nmap`, `nikto`, `wapiti`, `zap-cli`, and `dsniff` (for ARP spoofing)  
- **Firewall with Cockpit UI** for real-time management (`http://localhost:9090`)  
- **Centralized logging via Splunk** on `http://localhost:8001`  
- **DVWA** running on victim node at `http://localhost:8000`  
- **Network segmentation** enforced by Docker bridge networks and firewall rules  
- **Real-time packet inspection** and log forwarding via `rsyslog` and `iptables`  
- **Graphical network visualization** with Streamlit + PyVis:
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

# 5. Access the attacker container to run security tools
docker exec -it attacker bash

# 6. Launch the network visualizer (Streamlit GUI)
streamlit run network_gui.py

# 7. Access the main services in your browser
DVWA Victim:  http://localhost:8000  
IoT Camera:   http://localhost:8081  
IoT Thermostat: http://localhost:8082  
Firewall Cockpit: http://localhost:9090  
Splunk UI:    http://localhost:8001
