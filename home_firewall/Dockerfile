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

CMD ["sleep", "infinity"]