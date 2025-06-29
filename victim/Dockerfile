FROM php:7.4-apache


ENV DEBIAN_FRONTEND=noninteractive


RUN apt-get update && \
    apt-get install -y git mariadb-server unzip curl \
    libzip-dev libpng-dev libjpeg-dev libonig-dev libxml2-dev && \
    docker-php-ext-install mysqli && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


RUN git clone https://github.com/digininja/DVWA.git /var/www/html


RUN chown -R www-data:www-data /var/www/html && \
    chmod -R 755 /var/www/html && \
    cp /var/www/html/config/config.inc.php.dist /var/www/html/config/config.inc.php

EXPOSE 80

COPY startup.sh /startup.sh
RUN chmod +x /startup.sh
ENTRYPOINT ["/startup.sh"]
CMD ["sleep", "infinity"]