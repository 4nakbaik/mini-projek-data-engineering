#!/bin/bash

LOG_FILE="../logs/prepare.log"

echo "Pipeline started: $(date)" >> $LOG_FILE

python3 extract_sample.py >> $LOG_FILE 2>&1

if [ $? -ne 0 ]; then
    echo "Pipeline failed at $(date)" >> $LOG_FILE
    exit 1
fi

echo "Pipeline finished successfully at $(date)" >> $LOG_FILE