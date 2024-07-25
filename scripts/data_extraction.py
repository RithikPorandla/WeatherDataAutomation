import requests
import pandas as pd
import logging

def extract_weather_data(api_key, city):
    try:
        api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        df = pd.json_normalize(data)  # Normalize the JSON structure
        df.to_csv('C:/Users/Dell/Desktop/WeatherDataAutomation/data/extracted_weather_data.csv', index=False)
        print(df.head())  # Print DataFrame to check the structure
        logging.info("Weather data extracted and saved to extracted_weather_data.csv")
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch data from API: {e}")

if __name__ == "__main__":
    logging.basicConfig(filename='C:/Users/Dell/Desktop/WeatherDataAutomation/logs/data_extraction.log', level=logging.INFO)
    api_key = "c4bc73ecd182e2e3b9b5c3ed93681a92"  # Replace with your OpenWeatherMap API key
    city = "London"
    extract_weather_data(api_key, city)
