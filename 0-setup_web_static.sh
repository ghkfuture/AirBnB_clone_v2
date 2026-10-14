#!/usr/bin/env bash
# Sets up web servers for web_static deployment
if ! command -v nginx &> /dev/null; then
    apt-get update -y
    apt-get install nginx -y
fi
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "<html>
  <head>
  </head>
  <body>
    School
  </body>
</html>" > /data/web_static/releases/test/index.html
if [ -L /data/web_static/current ]; then
    rm /data/web_static/current
fi
ln -s /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
nginx_config="/etc/nginx/sites-available/default"
if ! grep -q "location /hbnb_static" "$nginx_config"; then
    sed -i '/server_name _;/a \ \n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' "$nginx_config"
fi
service nginx restart
exit 0
