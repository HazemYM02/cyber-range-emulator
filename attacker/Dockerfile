FROM debian:bullseye

ENV DEBIAN_FRONTEND=noninteractive

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
      ca-certificates && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

CMD ["sleep", "infinity"]