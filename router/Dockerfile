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
    wget \
    ca-certificates \
    procps \ 
 && apt clean

# Download and install Splunk Universal Forwarder
RUN wget -O splunkforwarder.tgz "https://download.splunk.com/products/universalforwarder/releases/10.0.0/linux/splunkforwarder-10.0.0-e8eb0c4654f8-linux-amd64.tgz" && \
    tar -xzf splunkforwarder.tgz -C /opt && \
    rm splunkforwarder.tgz

# Add Splunk to PATH
ENV PATH="/opt/splunkforwarder/bin:${PATH}"

WORKDIR /opt
CMD ["sleep", "infinity"]