#!/bin/bash

TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
PROJECT_NAME="project"  # Replace this with your actual project name

# Check the Celery status using inspect ping
if celery -A "${PROJECT_NAME}" inspect ping; then
    STATUS="Success"
else
    STATUS="Failure"
fi

OUTPUT='{"name":"Celery","time":"'${TIMESTAMP}'","status":"'${STATUS}'"}'

# Add logic here to send OUTPUT to your dashboard or perform other actions

# Echo the OUTPUT variable to the terminal
echo "$OUTPUT"
