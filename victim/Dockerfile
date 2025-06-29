FROM php:7.4-apache

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && \
    apt-get install -y git mariadb-server unzip curl \
    libzip-dev libpng-dev libjpeg-dev libonig-dev libxml2-dev && \
    docker-php-ext-install mysqli && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Clone DVWA
RUN git clone https://github.com/digininja/DVWA.git /var/www/html

# Set permissions and config
RUN chown -R www-data:www-data /var/www/html && \
    chmod -R 755 /var/www/html && \
    cp /var/www/html/config/config.inc.php.dist /var/www/html/config/config.inc.php

# Expose DVWA on port 80
EXPOSE 80

CMD ["apache2-foreground"]