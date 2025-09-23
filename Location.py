from geopy.geocoders import Nominatim
import requests


geolocator = Nominatim(user_agent="weather_app")
location = geolocator.geocode("Carroll, Iowa")

print(location.latitude, location.longitude)