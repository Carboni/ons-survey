#!/bin/bash

while [ true ]
do
    curl -i http://localhost:5000/
    for access_code in $(echo 1 2 3 4)
    do
      curl -i \
      http://ons-survey.herokuapp.com/code?access_code=$access_code
    done

    sleep 1
done
