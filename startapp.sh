#!/bin/bash
source /var/www/myapp/venv/bin/activate
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app