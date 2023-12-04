#!/bin/bash

TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
CELERY_BEAT_PID_FILE="celery-beat.pid"

# Check if PID file exists
if [ -e "$CELERY_BEAT_PID_FILE" ]; then
    STATUS="Running"
else
    STATUS="Failure"
fi

OUTPUT='{"name":"Celery-Beat","time":"'${TIMESTAMP}'","status":"'${STATUS}'"}'

# Add logic here to send OUTPUT to your dashboard or perform other actions

# Echo the OUTPUT variable to the terminal
echo "$OUTPUT"