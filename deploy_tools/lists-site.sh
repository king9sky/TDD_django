#!/bin/bash
/usr/local/nginx/sbin/nginx
cd /home/sites/superlists-staging.com/source
/home/sites/superlists-staging.com/virtualenv/bin/gunicorn --bind unix:/tmp/47.105.180.65.socket TDDweb.wsgi:application