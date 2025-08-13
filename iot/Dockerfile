FROM debian:bullseye

# Install base tools
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    iproute2 \
    iputils-ping \
    net-tools \
    netcat-traditional \
    curl \
    nano \
    python3 \
    python3-pip \
    tcpdump \
    && apt-get clean && rm -rf /var/lib/apt/lists/*


COPY startup.sh /opt/startup.sh
RUN chmod +x /opt/startup.sh

# Set working directory
WORKDIR /opt

CMD ["sleep", "infinity"]
