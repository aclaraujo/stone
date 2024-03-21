#!/bin/bash

echo "Running job extract_files.py"
/opt/jobs/extract_files.py
echo "Running job ingest_bronze.py"
/opt/jobs/ingest_bronze.py
echo "Running job ingest_silver.py"
/opt/jobs/ingest_silver.py
echo "Running job ingest_gold.py"
/opt/jobs/ingest_gold.py