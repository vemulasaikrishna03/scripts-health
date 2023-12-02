#!/bin/bash

TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

if curl -f http://localhost; then
    STATUS="Success"
    exit 0 
else
    STATUS="Failure"
    exit 1  
    
fi

OUTPUT='{"name":"Nginx-server","time":"'${TIMESTAMP}'","status":"'${STATUS}'"}'

#todo::send the output to dashbord
