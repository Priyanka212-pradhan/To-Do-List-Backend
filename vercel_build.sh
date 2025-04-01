#!/bin/bash

# Install Python dependencies (including psycopg2 for PostgreSQL)
pip3 install -r requirements.txt

# Apply database migrations
python3 manage.py migrate

# Collect static files
python3 manage.py collectstatic --noinput
