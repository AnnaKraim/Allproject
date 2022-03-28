#!/bin/bash
echo "ft_server starting"
service mysql start

echo "CREATE DATABASE wordpress;" | mysql
echo "CREATE USER 'csherril'@'localhost' IDENTIFIED BY 'kXzqP3dDdeIpAsU';" | mysql
echo "GRANT ALL ON wordpress.* TO 'csherril'@'localhost' IDENTIFIED BY 'kXzqP3dDdeIpAsU' WITH GRANT OPTION;" | mysql
echo "FLUSH PRIVILEGES;" | mysql

service nginx start
service php7.3-fpm start
bash
