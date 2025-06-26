FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y iproute2 iputils-ping iptables quagga tcpdump && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Enable IP forwarding on boot
RUN echo "net.ipv4.ip_forward=1" >> /etc/sysctl.conf

CMD ["sleep", "infinity"]