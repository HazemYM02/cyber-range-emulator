FROM debian:bullseye

ENV DEBIAN_FRONTEND=noninteractive

# Install core tools and deps
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      iproute2 iputils-ping net-tools curl gnupg nmap netcat-traditional \
      lsb-release ca-certificates python3 python3-pip python3-venv nano git \
      openjdk-11-jre-headless \
      wapiti dsniff tcpdump arping iptables && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Optional: ZAP CLI client only (ZAP daemon runs in a separate container)
RUN pip3 install --no-cache-dir zapcli

# Nikto
RUN git clone https://github.com/sullo/nikto.git /opt/nikto && \
    ln -s /opt/nikto/program/nikto.pl /usr/local/bin/nikto && \
    chmod +x /usr/local/bin/nikto

# Helper scripts
COPY tools/ /opt/tools/
# don’t fail if no *.sh yet
RUN chmod +x /opt/tools/*.sh || true

# Your files
COPY startup.sh /opt/startup.sh
RUN chmod +x /opt/startup.sh

COPY pentest_auto.py /opt/pentest_auto.py
COPY nmap_nikto.py /opt/nmap_nikto.py

WORKDIR /opt
CMD ["sleep", "infinity"]