import pandas as pd
from sqlalchemy import create_engine
import logging

def load_data_to_db(input_file, db_url, table_name):
    try:
        df = pd.read_csv(input_file)
        engine = create_engine(db_url)
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        logging.info(f"Weather data loaded into {table_name} table in the database")
    except Exception as e:
        logging.error(f"Failed to load data into database: {e}")

if __name__ == "__main__":
    logging.basicConfig(filename='C:/Users/Dell/Desktop/WeatherDataAutomation/logs/data_loading.log', level=logging.INFO)
    input_file = 'C:/Users/Dell/Desktop/WeatherDataAutomation/data/transformed_weather_data.csv'
    db_url = 'sqlite:///../data/weather_database.db'
    table_name = 'weather_data'
    load_data_to_db(input_file, db_url, table_name)
