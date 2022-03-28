FROM debian:buster

RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y install nginx && \ 
    apt-get -y install wget && \
    apt-get -y install mariadb-server mariadb-client && \
    apt-get -y install php php-fpm php-mysql php-mbstring php-gd php-cli \ 
                       php7.3-gmp php7.3-curl php7.3-intl php7.3-xmlrpc php7.3-xml php7.3-zip php7.3-common && \
    apt-get -y install vim

RUN mkdir /var/www/localhost
ADD https://files.phpmyadmin.net/phpMyAdmin/5.0.4/phpMyAdmin-5.0.4-all-languages.tar.gz phpMyAdmin.tar.gz
RUN tar -xf phpMyAdmin.tar.gz && mv phpMyAdmin-5.0.4-all-languages phpmyadmin && mv phpmyadmin /var/www/localhost/ && rm phpMyAdmin.tar.gz && \
    mv /var/www/localhost/phpmyadmin/config.sample.inc.php /var/www/localhost/phpmyadmin/config.inc.php

ADD https://ru.wordpress.org/latest-ru_RU.tar.gz wordpress.tar.gz
RUN tar -xf wordpress.tar.gz && mv wordpress /var/www/localhost/ && rm wordpress.tar.gz 
COPY /srcs/wp-config.php /var/www/localhost/wordpress

COPY /srcs/nginx.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/nginx.conf /etc/nginx/sites-enabled/nginx.conf && \
    rm /etc/nginx/sites-available/default && rm /etc/nginx/sites-enabled/default

RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/ssl/private/nginx-selfsigned.key -out /etc/ssl/certs/nginx-selfsigned.crt\
    -subj "/C=RU/ST=Moscow/L=Moscow/O=42/OU=21/ON=nginx-selfsigned" 

COPY ./srcs/start.sh ./
CMD ["bash", "/start.sh"]