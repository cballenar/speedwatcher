#!/usr/bin/env bash
# Source: https://gist.github.com/asmerkin/df919a6a79b081512366

# Updating packages
apt-get update

# dependencies
apt-get install -y python-dev python-pip
pip install virtualenv flask flask_restful flask-mysql


# ---------------------------------------
#          MySQL Setup
# ---------------------------------------

# Setting MySQL root user password root/root
debconf-set-selections <<< 'mysql-server mysql-server/root_password password root'
debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password root'

# Installing packages
apt-get install -y mysql-server mysql-client libmysqlclient-dev


# ---------------------------------------
#       Tools Setup
# ---------------------------------------

# Customize bash
echo "
# Color me!
export PS1='\e[1;32m\n\u@\h: \e[0;33m\w\n\e[m→ '" >> /home/vagrant/.profile
