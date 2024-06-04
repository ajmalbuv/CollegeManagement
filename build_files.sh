#!/bin/bash

# Build the project
echo "Building the project..."
apt-get update 
/usr/local/bin/pip3 install -r requirements.txt
echo "Make Migration..."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

echo "Collect Static..."
python3 manage.py collectstatic --noinput --clear