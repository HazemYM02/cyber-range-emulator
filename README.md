# Cyber-Range Emulator

A modular, Docker-based cybersecurity training and testing environment simulating a segmented enterprise network. Designed for students, educators, and researchers to practice real-world cyber operations in a safe and isolated environment.

---

## Project Objectives

- 🔄 Simulate a multi-zone network (attacker, internal, services)
- 🧑‍💻 Support offensive/defensive tools like Nmap, Snort, Metasploit, and DVWA
- 🔎 Enable realistic testing of attacks, scans, and routing/firewall behavior
- 🖼️ Visualize network topology dynamically via a custom Streamlit GUI
- ⚙️ Allow automation via Python scripting and Docker SDK
- 📁 Integrate logging and capture for incident response testing

---

## Technologies Used

- **Docker + Docker Compose** — containerized infrastructure
- **Python** — with Docker SDK, Streamlit, PyVis
- **DVWA** — Damn Vulnerable Web App
- **Snort**, **Netcat**, **Nmap**, **Metasploit** — security testing tools
- **tcpdump** — for live packet capture
- **Wireshark** — for `.pcap` analysis

---

## 🌐 Network Topology

The network is segmented into three bridges:

| Network        | CIDR Range       | Purpose                       |
|----------------|------------------|-------------------------------|
| `net_attacker` | 172.28.0.0/24    | Offensive network             |
| `net_internal` | 172.29.0.0/24    | Victims, firewall, workstation|
| `net_services` | 172.30.0.0/24    | DNS, DVWA, SIEM               |

### 📦 Key Containers

| Container   | Role                  | IP Address     | Network(s)       |
|-------------|-----------------------|----------------|------------------|
| `attacker`  | Launches attacks      | 172.28.0.10    | net_attacker     |
| `victim`    | DVWA target system    | 172.29.0.10    | net_internal     |
| `victim1`   | Additional DVWA node  | 172.29.0.11    | net_internal     |
| `victim2`   | Additional DVWA node  | 172.29.0.12    | net_internal     |
| `firewall`  | Filtering system      | 172.29.0.30    | net_internal     |
| `workstation`| Simulated user host  | 172.29.0.60    | net_internal     |
| `dns`       | DNS server            | 172.30.0.50    | net_services     |
| `webserver` | Hosts DVWA            | 172.30.0.40    | net_services     |
| `siem`      | Collects logs         | 172.30.0.70    | net_services     |
| `router`    | Routes traffic        | 172.28/29/30.254 | all 3 networks |

---

## Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/HazemYM02/cyber-range-emulator.git
cd cyber-range-emulator

# 2. Build all Docker containers
docker compose build

# 3. Launch the environment
docker compose up -d

# 4. Open the visual GUI in your browser
streamlit run network_gui.py
