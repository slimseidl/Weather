import requests
import json 
from datetime import datetime
from geopy import Nominatim

geolocator = Nominatim(user_agent="my_geocoder")


class WeatherData():
    def __init__(self,latitude=0.0, longitude=0.0,month=None, day=None,years=[datetime.now().year-5,datetime.now().year-4, datetime.now().year-3, datetime.now().year-2, datetime.now().year-1]):
        self.latitude = latitude
        self.longitude = longitude
        self.day = day
        self.month = month
        self.years = years


    def get_weather(self):
        daily_weather_over_years = []
        for year in self.years:
            response = requests.get(f'https://archive-api.open-meteo.com/v1/archive?latitude={self.latitude}&longitude={self.longitude}'
                                f'&start_date={year}-{self.month}-{self.day}&end_date={year}-{self.month}-{self.day}'
                                f'&daily=temperature_2m_mean,precipitation_sum,wind_speed_10m_max,'
                                f'temperature_2m_max,temperature_2m_min'
                                f'&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch') # ADD A MAX AND MIN TEMP FOR RECORDS
            
            if response.status_code == 200:
                weather_data = response.json()

                
                daily_weather_data = {
                    "Date": weather_data["daily"]["time"][0],
                    "Avg Temp": weather_data["daily"]["temperature_2m_mean"][0],
                    "Max Wind": weather_data["daily"]["wind_speed_10m_max"][0],
                    "Precipitation": weather_data["daily"]["precipitation_sum"][0],
                    "Max Temp": weather_data["daily"]["temperature_2m_max"][0],
                    "Min Temp": weather_data["daily"]["temperature_2m_min"][0]
                }

                daily_weather_over_years.append(daily_weather_data)


            else:
                print(f'Could not obtain weather data with response code {response.status_code}')
    
        return daily_weather_over_years


    def get_average_temp(self):
        weather_info = self.get_weather()
        temps = [day["Avg Temp"] for day in weather_info]

        if temps:
            return sum(temps) / len(temps)
        else:
            return None
        
    
    def get_wind_speed(self):
        weather_info = self.get_weather()
        wind = [day["Max Wind"] for day in weather_info]

        if wind:
            return sum(wind) / len(wind)
        else:
            return None 
        
    def get_precip(self):
        weather_info = self.get_weather()
        precip = [day["Precipitation"] for day in weather_info]

        if precip:
            return sum(precip) / len(precip)
        else:
            return None 
        
    def get_min_temp(self):
        weather_info = self.get_weather()
        minTemp = [day["Min Temp"] for day in weather_info]
        return min(minTemp)

    def get_max_temp(self):
        weather_info = self.get_weather()
        maxTemp = [day["Max Temp"] for day in weather_info]
        return max(maxTemp)

        
    def print_info(self):
        latitude = self.latitude
        longitude = self.longitude

        location = geolocator.reverse((latitude,longitude),exactly_one=True)

        if location and "address" in location.raw:
            city = location.raw["address"].get("city", "")
            state = location.raw["address"].get("state","")

        # print(f'The average temperature on {datetime.strptime((self.month + "/" + self.day),"%m/%d").strftime("%B %d")} for {city}, {state} over the last 5 years is {self.get_average_temp():.1f} degrees Farenheit.')
        # print(f'The average max wind speed on {datetime.strptime((self.month + "/" + self.day),"%m/%d").strftime("%B %d")} for {city}, {state} over the last 5 years is {self.get_wind_speed():.2f} mph.')
        # print(f'The average total precipitation on {datetime.strptime((self.month + "/" + self.day),"%m/%d").strftime("%B %d")} for {city}, {state} over the last 5 years is {self.get_precip():.2f}"')
        
        print(f'Weather information for {city}, {state} on {datetime.strptime((self.month + "/" + self.day),"%m/%d").strftime("%B %d")} over the last 5 years:\n'
              f'\t-Average Temperature: {self.get_average_temp():.1f} degrees Farenheit\n'
              f'\t-Maximum Temperature: {self.get_max_temp():.1f} degrees Farenheit\n'
              f'\t-Minimum Temperature: {self.get_min_temp():.1f} degrees Farenheit\n'
              f'\t-Average Max Wind Speed: {self.get_wind_speed():.2f} mph\n'
              f'\t-Average Total Precipitation: {self.get_precip():.2f}"')
    





        