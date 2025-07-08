FROM php:7.4-apache

ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies for PHP and DVWA
RUN apt-get update && \
    apt-get install -y \
        git \
        unzip \
        curl \
        libzip-dev \
        libpng-dev \
        libjpeg-dev \
        libonig-dev \
        libxml2-dev \
        mariadb-client \
        libssl-dev \
        libcurl4-openssl-dev \
        pkg-config && \
    docker-php-ext-install mysqli && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Clone DVWA
RUN git clone https://github.com/digininja/DVWA.git /var/www/html

# Set permissions and config
RUN chown -R www-data:www-data /var/www/html && \
    chmod -R 755 /var/www/html && \
    cp /var/www/html/config/config.inc.php.dist /var/www/html/config/config.inc.php

COPY startup.sh /startup.sh
RUN chmod +x /startup.sh

ENTRYPOINT ["/startup.sh"]
CMD ["sleep", "infinity"]