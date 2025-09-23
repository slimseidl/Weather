from geopy.geocoders import Nominatim
import requests
from Weather import WeatherData


geolocator = Nominatim(user_agent="weather_app")


city = input(f'Enter City: \n')
state = input(f'Enter State: \n')
location = geolocator.geocode(f'{city}, {state}')
latitude = location.latitude
longitude = location.longitude
day = input()
month = input()
year = input()



