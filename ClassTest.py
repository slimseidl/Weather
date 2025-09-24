from geopy.geocoders import Nominatim
import requests
from Weather import WeatherData


geolocator = Nominatim(user_agent="weather_app")


city = input(f'Enter City: \n')
state = input(f'Enter State: \n')
location = geolocator.geocode(f'{city}, {state}')
latitude = location.latitude
longitude = location.longitude
monthday = input("Enter a month and day in the following format: mm/dd\n").split("/")

# print(monthday[0], monthday[1])
weatherCheck = WeatherData(latitude, longitude, monthday[0], monthday[1])

weatherCheck.get_weather
weatherCheck.get_average_temp()
weatherCheck.get_wind_speed()

weatherCheck.print_info()





