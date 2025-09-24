# contains build code before putting into a class 

import requests 
import json
from geopy.geocoders import Nominatim



geolocator = Nominatim(user_agent="weather_app")


city = input(f'Enter City: \n')
state = input(f'Enter State: \n')
location = geolocator.geocode(f'{city}, {state}')
latitude = location.latitude
longitude = location.longitude
years = [2020, 2021, 2022, 2023, 2024] # Convert to last 5 years dynamically / datetime.now.year - 1 / year - 5
day = input("Enter a day:\n")
month = input("Enter a month number:\n")


daily_weather_over_years = [] 
for year in years: 
    response = requests.get(f'https://archive-api.open-meteo.com/v1/archive?latitude={latitude}&longitude={longitude}' #API Call
                        f'&start_date={year}-{month}-{day}&end_date={year}-{month}-{day}' # start / end are same just loops different years
                        f'&daily=temperature_2m_mean,precipitation_sum,wind_speed_10m_max'
                        f'&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch')
    
    if response.status_code == 200:
        weather_data = response.json()

        for i in range(len(weather_data["daily"]["time"])):
            daily_weather_data = {
                "Date": weather_data["daily"]["time"][i],
                "Avg Temp": weather_data["daily"]["temperature_2m_mean"][i],
                "Max Wind": weather_data["daily"]["wind_speed_10m_max"][i],
                "Precipitation": weather_data["daily"]["precipitation_sum"][i]
            }

            daily_weather_over_years.append(daily_weather_data)

