FROM debian:bullseye

# Install networking tools, logging, firewall, cockpit
RUN apt update && apt install -y \
    iproute2 \
    iputils-ping \
    nano \
    net-tools \
    tcpdump \
    traceroute \
    ufw \
    iptables \
    cockpit \
    cockpit-networkmanager \
    sudo \
 && apt clean

# Create cockpit login user
RUN useradd -m -s /bin/bash cyberadmin && \
    echo 'cyberadmin:cyberpass' | chpasswd && \
    usermod -aG sudo cyberadmin

# Expose Cockpit Web UI port
EXPOSE 9090

# Start Cockpit Web Service + UFW + routing
CMD ["sh", "-c", "\
  echo 1 > /proc/sys/net/ipv4/ip_forward && \
  ufw --force enable && \
  ufw logging on && \
  ufw default deny incoming && \
  ufw allow out on eth0 && \
  /usr/lib/cockpit/cockpit-ws --no-tls & \
  sleep infinity"]