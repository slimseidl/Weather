import requests
import json 


class WeatherData():
    def __init__(self,latitude=0.0, longitude=0.0,day=None,month=None,year=None):
        self.latitude = latitude
        self.longitude = longitude
        self.day = day
        self.month = month
        self.year = year


    def get_weather(self):
        daily_weather_over_years = []
        for year in self.year:
            response = requests.get(f'https://archive-api.open-meteo.com/v1/archive?latitude={self.latitude}&longitude={self.longitude}'
                                f'&start_date={self.year}-{self.month}-{self.day}&end_date={self.year}-{self.month}-{self.day}'
                                f'&daily=temperature_2m_mean,temperature_2m_max,temperature_2m_min,precipitation_sum,wind_speed_10m_max'
                                f'&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch')
            
            if response.status_code == 200:
                weather_data = response.json()

                for i in range(len(weather_data["daily"]["time"])):
                    daily_weather_data = {
                        "Year": weather_data["daily"]["time"][i],
                        "Avg Temp": weather_data["daily"]["temperature_2m_mean"][i],
                        "Max Wind": weather_data["daily"]["wind_speed_10m_max"][i],
                        "Precipitation": weather_data["daily"]["precipitation_sum"][i]
                    }

                    daily_weather_over_years.append(daily_weather_data)


            else:
                print(f'Could not obtain weather data with response code {response.status_code}')







        