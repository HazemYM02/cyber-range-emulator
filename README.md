# Cyber-Range Emulator

A modular, Docker-based cybersecurity training and testing environment that simulates a realistic, multi-zone network infrastructure. This project is designed to help students, educators, and security researchers learn and practice networking, penetration testing, and threat detection techniques in a safe, controlled environment.

---

## 🎯 Project Goals

- ✅ Simulate a segmented enterprise-like network using Docker  
- ✅ Include attacker, victim, firewall, and SIEM roles  
- ✅ Enable realistic cyber attack simulation (e.g., scanning, exploitation)  
- ✅ Visualize the network in real-time via a custom GUI  
- ✅ Provide a scriptable Python interface for automation and control  
- ✅ Support educational exercises using tools like DVWA, Snort, Nmap, Netcat, and Metasploit  

---

## 🔧 Technologies Used

- Docker & Docker Compose  
- Python (Streamlit, PyVis, Docker SDK)  
- DVWA (Damn Vulnerable Web Application)  
- Snort, Nmap, Netcat, Metasploit  

---

## 🖥️ Network Design

- `net_attacker`: Attacker zone (172.28.0.0/24)  
- `net_internal`: Internal network (172.29.0.0/24)  
- `net_services`: DNS, Web, SIEM (172.30.0.0/24)  

| Container     | Role                  | IP Address       | Network        |
|---------------|-----------------------|------------------|----------------|
| attacker      | Offensive tools       | 172.28.0.10      | net_attacker   |
| victim        | Exploitable system    | 172.29.0.10      | net_internal   |
| firewall      | Packet filtering      | 172.29.0.30      | net_internal   |
| workstation   | Internal user system  | 172.29.0.60      | net_internal   |
| webserver     | DVWA host             | 172.30.0.40      | net_services   |
| dns           | DNS server            | 172.30.0.50      | net_services   |
| siem          | Log aggregation       | 172.30.0.70      | net_services   |
| router        | Gateway between zones | 172.x.x.254      | all subnets    |

---

## 🚀 Getting Started

```bash
git clone https://github.com/your-username/cyber-range-emulator.git
cd cyber-range-emulator

# Build and launch the network
docker compose build
docker compose up -d

# Launch GUI to visualize network
streamlit run network_gui.py
