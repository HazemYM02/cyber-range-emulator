FROM debian:bullseye


ENV DEBIAN_FRONTEND=noninteractive

# Install useful tools for log monitoring and forwarding
RUN apt-get update && \
    apt-get install -y \
    rsyslog \
    iproute2 \
    iputils-ping \
    net-tools \
    tcpdump \
    curl \
    vim \
    procps && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY startup.sh /startup.sh
RUN chmod +x /startup.sh


ENTRYPOINT ["/startup.sh"]


CMD ["rsyslogd", "-n"]