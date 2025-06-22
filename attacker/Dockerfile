FROM kalilinux/kali-rolling

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y nmap metasploit-framework iputils-ping && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

CMD ["sleep", "infinity"]