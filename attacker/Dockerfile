FROM debian:bullseye

ENV DEBIAN_FRONTEND=noninteractive

# Install core tools and dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      iproute2 \
      iputils-ping \
      net-tools \
      curl \
      gnupg \
      nmap \
      netcat-traditional \
      lsb-release \
      ca-certificates \
      python3 \
      python3-pip \
      nano \
      git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Nikto manually from GitHub
RUN git clone https://github.com/sullo/nikto.git /opt/nikto && \
    ln -s /opt/nikto/program/nikto.pl /usr/local/bin/nikto && \
    chmod +x /usr/local/bin/nikto

# Copy user scripts
COPY pentest_auto.py /opt/pentest_auto.py
COPY nmap_nikto.py /opt/nmap_nikto.py


WORKDIR /opt

CMD ["sleep", "infinity"]