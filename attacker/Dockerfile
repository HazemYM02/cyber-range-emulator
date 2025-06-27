FROM kalilinux/kali-rolling

# Set non-interactive frontend to prevent hangs
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y \
      nmap \
      netcat-traditional \
      curl \
      iputils-ping \
      gnupg \
      lsb-release && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

CMD ["sleep", "infinity"]