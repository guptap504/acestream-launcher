#! /bin/bash

# Installing acestream-launcher

mkdir -p /opt/acestream-launcher
mv acestream.py /opt/acestream-launcher
install --mode=0644 acestream /usr/bin/