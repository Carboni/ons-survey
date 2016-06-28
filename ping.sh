#!/bin/bash

while [ true ]
do
    for access_code in $(echo 1 2 3 4)
    do
      curl -i \
      http://localhost:5000/?access_code=$access_code
    done

    sleep 1
done
