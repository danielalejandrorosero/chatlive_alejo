#!/usr/bin/env bash
# exit on error
set -o errexit
echo "Ejecutando pip install..."
pip install -r requirements.txt
echo "Ejecutando collectstatic..."
python manage.py collectstatic --no-input
echo "Ejecutando migrate..."
python manage.py migrate