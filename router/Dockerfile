FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y iproute2 iputils-ping iptables quagga tcpdump && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


RUN echo "net.ipv4.ip_forward=1" >> /etc/sysctl.conf

COPY startup.sh /startup.sh
RUN chmod +x /startup.sh
ENTRYPOINT ["/startup.sh"]
CMD ["sleep", "infinity"]