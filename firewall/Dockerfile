FROM debian:bullseye

RUN apt update && apt install -y \
    iproute2 \
    iputils-ping \
    net-tools \
    traceroute \
    tcpdump \
    iptables \
    nftables \
    nano \
 && apt clean

CMD ["sleep", "infinity"]