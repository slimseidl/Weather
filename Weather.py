import requests
import json 


class WeatherData():
    def __init__(self,latitude=0.0, longitude=0.0,day=None,month=None,years=[20]):
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
                                f'&daily=temperature_2m_mean,precipitation_sum,wind_speed_10m_max'
                                f'&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch')
            
            if response.status_code == 200:
                weather_data = response.json()

                
                daily_weather_data = {
                    "Date": weather_data["daily"]["time"][0],
                    "Avg Temp": weather_data["daily"]["temperature_2m_mean"][0],
                    "Max Wind": weather_data["daily"]["wind_speed_10m_max"][0],
                    "Precipitation": weather_data["daily"]["precipitation_sum"][0]
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
        
    





        