FROM debian:bullseye

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      iproute2 \
      iptables \
      iputils-ping \
      net-tools \
      tcpdump \
      nano \
      python3 \
      python3-pip \
      rsyslog \
      kmod \
      procps \
      vim && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Enable logging service
RUN systemctl enable rsyslog || true

# Create monitoring script
COPY monitor.py /opt/monitor.py
COPY startup.sh /startup.sh
RUN chmod +x /startup.sh /opt/monitor.py

WORKDIR /opt

ENTRYPOINT ["/startup.sh"]
CMD ["sleep", "infinity"]