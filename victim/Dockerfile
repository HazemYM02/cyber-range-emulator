FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y vsftpd netcat iputils-ping && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

CMD ["sleep", "infinity"]