
### tests/test_scripts.py

import unittest
import os
import pandas as pd
from scripts import data_extraction, data_transformation, data_loading

class TestETLScripts(unittest.TestCase):

    def test_data_extraction(self):
        data_extraction.extract_weather_data('your_openweathermap_api_key', 'London')
        self.assertTrue(os.path.exists('../data/extracted_weather_data.csv'))

    def test_data_transformation(self):
        data_transformation.transform_weather_data('../data/extracted_weather_data.csv', '../data/transformed_weather_data.csv')
        df = pd.read_csv('../data/transformed_weather_data.csv')
        self.assertFalse(df.isnull().values.any())

    def test_data_loading(self):
        db_url = 'sqlite:///../data/test_weather_database.db'
        data_loading.load_data_to_db('../data/transformed_weather_data.csv', db_url, 'test_weather_data')
        engine = data_loading.create_engine(db_url)
        df = pd.read_sql_table('test_weather_data', con=engine)
        self.assertTrue(len(df) > 0)

if __name__ == '__main__':
    unittest.main()
