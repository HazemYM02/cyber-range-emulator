FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y iproute2 iputils-ping curl cron && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Simulate user browsing by periodic curl to webserver
RUN echo "* * * * * root curl -s http://172.30.0.40 > /dev/null" >> /etc/crontab

CMD ["sleep", "infinity"]