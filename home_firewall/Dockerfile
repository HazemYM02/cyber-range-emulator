FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    iproute2 \
    iptables \
    rsyslog \
    net-tools \
    iputils-ping \
    tcpdump \
    nano \
    && apt-get clean

COPY startup.sh /startup.sh
RUN chmod +x /startup.sh

ENTRYPOINT ["/startup.sh"]
CMD ["sleep", "infinity"]