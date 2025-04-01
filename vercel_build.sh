#!/bin/bash

# Update apt package list and install dependencies
apt-get update || { echo "apt-get update failed"; exit 1; }

# Install Python 3, pip, and PostgreSQL development libraries
apt-get install -y python3 python3-pip libpq-dev || { echo "apt-get install failed"; exit 1; }

# Install Python dependencies
pip3 install -r requirements.txt || { echo "pip install failed"; exit 1; }

# Apply database migrations
python3 manage.py migrate || { echo "migrate failed"; exit 1; }

# Collect static files
python3 manage.py collectstatic --noinput || { echo "collectstatic failed"; exit 1; }
