#!/bin/bash

# Update apt package list and install dependencies
apt-get update

# Install Python 3, pip, and PostgreSQL development libraries
apt-get install -y python3 python3-pip libpq-dev

# Install Python dependencies
pip3 install -r requirements.txt

# Apply database migrations
python3 manage.py migrate

# Collect static files
python3 manage.py collectstatic --noinput
