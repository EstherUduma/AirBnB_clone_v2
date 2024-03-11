#!/usr/bin/env bash
# Sets up a web server for deployment of web_static.

# Update package list and install nginx
apt-get update
apt-get install -y nginx

# Create necessary directories and an index.html file
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Holberton School" > /data/web_static/releases/test/index.html

# Create a symbolic link to the latest version
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change ownership and group of /data directory
chown -R ubuntu /data/
chgrp -R ubuntu /data/

# Configure Nginx server block with aliases and custom error pages
printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

# Restart the Nginx service to apply changes
service nginx restart
