#!/usr/bin/env bash

#Principais
sudo apt-get install git python2.7 postgresql nano python-virtualenv xfonts-75dpi
#Relatórios
mkdir /tmp/odoo
cd /tmp/odoo
wget http://ftp.us.debian.org/debian/pool/main/libj/libjpeg-turbo/libjpeg62-turbo_1.3.1-12_amd64.deb
wget http://nightly.odoo.com/extra/wkhtmltox-0.12.1.2_linux-jessie-amd64.deb
sudo dpkg -i *.deb
#build
sudo apt-get install gcc python2.7-dev libxml2-dev \
    libxslt1-dev libevent-dev libsasl2-dev libldap2-dev libpq-dev \
    libpng12-dev libjpeg-dev
#node
sudo apt-get install -y npm
sudo npm install -g less
#postgres
sudo -u postgres createuser --createdb $(whoami)
createdb $(whoami)
