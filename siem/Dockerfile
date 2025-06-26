FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y rsyslog tcpdump iputils-ping && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Enable rsyslog in foreground mode
CMD ["rsyslogd", "-n"]