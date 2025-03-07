#!/bin/bash

PORT=8000

HEALTHCHECK_URL="http://localhost:${PORT}/docs#/"

RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" ${HEALTHCHECK_URL})

if [ "$RESPONSE" -eq 200 ]; then
    echo "Service is healthy"
    exit 0
else
    echo "Service is not healthy. Response code: $RESPONSE"
    exit 1
fi
