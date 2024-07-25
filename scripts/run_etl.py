import os
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(filename='C:/Users/Dell/Desktop/WeatherDataAutomation/logs/etl_log.log', level=logging.INFO)

def log_and_run(command):
    result = os.system(command)
    if result == 0:
        logging.info(f"{datetime.now()}: Successfully ran {command}")
    else:
        logging.error(f"{datetime.now()}: Failed to run {command} with exit code {result}")

def run_etl():
    # Step 1: Extract data
    log_and_run('python scripts/data_extraction.py')

    # Step 2: Transform data
    log_and_run('python scripts/data_transformation.py')

    # Step 3: Load data into database
    log_and_run('python scripts/data_loading.py')

if __name__ == "__main__":
    run_etl()
