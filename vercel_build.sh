#!/bin/bash

# Install Python (if it's not installed already)
apt-get update
apt-get install -y python3 python3-pip

# Install dependencies
pip3 install -r requirements.txt

# Apply database migrations
python3 manage.py migrate

# Collect static files
python3 manage.py collectstatic --noinput
