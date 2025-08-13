FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
SHELL ["/bin/bash", "-euxo", "pipefail", "-c"]

# Base tools + utils we need
RUN apt-get update && apt-get install -y --no-install-recommends \
    iproute2 iputils-ping nano net-tools tcpdump traceroute \
    ufw iptables sudo rsyslog ca-certificates curl gnupg \
    netcat-openbsd debconf-utils \
 && rm -rf /var/lib/apt/lists/*

# --- Preseed Snort so installation won't prompt (prevents exit code 100) ---
RUN apt-get update && \
    echo "snort snort/interface string any"               | debconf-set-selections && \
    echo "snort snort/address_range string 10.88.0.0/16"  | debconf-set-selections && \
    echo "snort snort/options string -A fast -l /var/log/snort -c /etc/snort/snort.conf" | debconf-set-selections && \
    echo "snort snort/disable_promisc boolean true"       | debconf-set-selections && \
    apt-get install -y --no-install-recommends snort && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && (apt-get install -y --no-install-recommends cockpit cockpit-network-manager || true) && \
    rm -rf /var/lib/apt/lists/*

# Snort basics: HOME_NET + a quick test rule
RUN sed -i 's|^ipvar[[:space:]]\+HOME_NET.*|ipvar HOME_NET [10.88.20.0/24,10.88.30.0/24]|' /etc/snort/snort.conf && \
    mkdir -p /etc/snort/rules && \
    printf 'alert icmp any any -> $HOME_NET any (msg:"ICMP test detected"; itype:8; sid:1000001; rev:1;)\n' \
      > /etc/snort/rules/local.rules

# Your startup script (starts Snort + Cockpit and pipes alerts to Splunk 9997)
COPY startup.sh /opt/startup.sh
RUN chmod +x /opt/startup.sh

EXPOSE 9090
CMD ["/opt/startup.sh"]

CMD ["sh", "-c", "\
  echo 1 > /proc/sys/net/ipv4/ip_forward && \
  ufw disable && \
  /usr/lib/cockpit/cockpit-ws --no-tls --address=0.0.0.0 --port=9090 --local-ssh & \
  sleep infinity"]