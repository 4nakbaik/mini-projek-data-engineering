#!/bin/bash

RAW_DIR="../data/raw/yellow_tripdata_2015-01.csv"
PROCESSED_DIR="../data/processed/sample_1.csv"
LOG_FILE="../logs/prepare.log"

echo "Pipeline started : $(date)" >> $LOG_FILE

python3 extract_sample.py >> $LOG_FILE 2>&1

echo "Pipeline finished : $(date)" >> $LOG_FILE