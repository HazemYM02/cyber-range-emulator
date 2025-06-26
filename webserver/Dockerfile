FROM php:7.4-apache

RUN apt-get update && \
    apt-get install -y git && \
    git clone https://github.com/digininja/DVWA /var/www/html && \
    chown -R www-data:www-data /var/www/html && \
    chmod -R 755 /var/www/html && \
    docker-php-ext-install mysqli

EXPOSE 80

CMD ["apache2-foreground"]