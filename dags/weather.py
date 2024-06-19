import os
import requests
from dotenv import load_dotenv
import csv
from datetime import datetime



def fetch_weather(api_key: str, city="Moscow") -> dict:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    weather_data = response.json()
    return weather_data

def weather_data_update(csv_path: str):
    load_dotenv(".env")
    api_key = os.getenv("API_KEY")
    city = "Moscow"
    new_data = fetch_weather(api_key=api_key, city=city)
    update = [
            (datetime.fromtimestamp(new_data['dt'])).strftime('%d.%m.%Y %H:%M'),
            new_data['name'],
            new_data['weather'][0]['main'],
            new_data['weather'][0]['description'],
            new_data['main']['temp'],
            new_data['main']['feels_like'],
            new_data['main']['pressure'],
            new_data['wind']['speed']
            ]
    
    with open(csv_path, mode='a', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow(update)
        

if __name__ == "__main__":
    # test weather API
    load_dotenv(".env")
    api_key = os.getenv("API_KEY")
    city = "Moscow"
    data = fetch_weather(api_key=api_key, city=city)
    print(data)
