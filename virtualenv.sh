#!/bin/bash

if [ -z "env" ]
then
  echo "Creating virtual environment..."
  virtualenv -p /usr/local/bin/python3 env
else
  echo "Virtual environment is present."
fi
source env/bin/activate
pip install -r requirements.txt
