#!/bin/bash

while [ true ]
do
    curl -i \
    -H "Content-Type: application/json" \
    -X GET -d '{"username":"xyz","password":"xyz"}' \
    http://localhost:5000/?access_code="test"
    
    sleep 1
done
