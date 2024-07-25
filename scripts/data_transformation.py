import pandas as pd
import logging

def transform_weather_data(input_file, output_file):
    try:
        df = pd.read_csv(input_file)
        
        # Example transformation: Extracting relevant fields and renaming columns
        transformed_df = pd.DataFrame({
            'city': df['name'],
            'temperature': df['main.temp'],
            'humidity': df['main.humidity'],
            'weather': df['weather'].apply(lambda x: eval(x)[0]['description'])
        })
        
        transformed_df.to_csv(output_file, index=False)
        logging.info(f"Weather data transformed and saved to {output_file}")
    except Exception as e:
        logging.error(f"Failed to transform data: {e}")

if __name__ == "__main__":
    logging.basicConfig(filename='C:/Users/Dell/Desktop/WeatherDataAutomation/logs/data_transformation.log', level=logging.INFO)
    input_file = 'C:/Users/Dell/Desktop/WeatherDataAutomation/data/extracted_weather_data.csv'
    output_file = 'C:/Users/Dell/Desktop/WeatherDataAutomation/data/transformed_weather_data.csv'
    transform_weather_data(input_file, output_file)
