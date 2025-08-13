FROM debian:bullseye

# Install Apache, PHP, Git, and dependencies
RUN apt-get update && \
    apt-get install -y apache2 php php-mysqli git curl unzip net-tools iproute2 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Enable Apache mod_rewrite
RUN a2enmod rewrite

# Clone DVWA with retry logic
RUN for i in 1 2 3; do \
      git clone --depth 1 https://github.com/digininja/DVWA.git /tmp/dvwa && break || sleep 5; \
    done && \
    rm -rf /var/www/html/* && \
    mv /tmp/dvwa/* /var/www/html/ && \
    mv /tmp/dvwa/.git /var/www/html/ && \
    cp /var/www/html/config/config.inc.php.dist /var/www/html/config/config.inc.php

# Set permissions
RUN chown -R www-data:www-data /var/www/html && \
    chmod -R 755 /var/www/html

# Copy startup script
COPY startup.sh /opt/startup.sh
RUN chmod +x /opt/startup.sh

# Set entrypoint
ENTRYPOINT ["/opt/startup.sh"]

# Expose Apache port
EXPOSE 80