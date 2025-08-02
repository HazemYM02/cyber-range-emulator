FROM php:7.4-apache

# Install required packages
RUN apt-get update && apt-get install -y \
    git unzip mariadb-client iputils-ping net-tools vim \
    && docker-php-ext-install mysqli

RUN apt-get update && apt-get install -y iproute2 iputils-ping

# Enable Apache rewrite
RUN a2enmod rewrite

# Clone DVWA into temporary location and move manually
RUN git clone https://github.com/digininja/DVWA.git /tmp/dvwa && \
    rm -rf /var/www/html/* && \
    mv /tmp/dvwa/* /var/www/html/ && \
    mv /tmp/dvwa/.git /var/www/html/

# Copy pre-created DVWA config from local host into container
COPY config/config.inc.php /var/www/html/config/config.inc.php

# Fix permissions
RUN chown -R www-data:www-data /var/www/html && \
    chmod -R 755 /var/www/html



EXPOSE 80

CMD ["sleep", "infinity"]

