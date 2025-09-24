from geopy.geocoders import Nominatim
import requests
from Weather import WeatherData
from sqlalchemy import create_engine, Integer, Float, Column
from sqlalchemy.orm import declarative_base, sessionmaker
from tabulate import tabulate


geolocator = Nominatim(user_agent="weather_app")


city = input(f'Enter City: \n')
state = input(f'Enter State: \n')
location = geolocator.geocode(f'{city}, {state}')
latitude = location.latitude
longitude = location.longitude
monthday = input("Enter a month and day in the following format: mm/dd\n").split("/")

WeatherForLocation = WeatherData(latitude, longitude, monthday[0], monthday[1])
weather_data = WeatherForLocation.get_weather()


base = declarative_base()

class WeatherRecords(base):
    __tablename__ = "Historical Weather Records"
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Latitude = Column(Float, nullable=False)
    Longitute = Column(Float, nullable=False)
    Month = Column(Integer,nullable=False)
    Day = Column(Integer,nullable=False)
    Years = Column(Integer,nullable=False)
    Avg_Temp = Column(Float)
    Max_Wind = Column(Float)
    Precipitation = Column(Float)
    Max_Temp = Column(Float)
    Min_Temp = Column(Float)


engine = create_engine('sqlite:///weather.db')


Session = sessionmaker(bind=engine)
session = Session()

for weather in weather_data:
    record = WeatherRecords(
        Latitude=latitude,
        Longitude=longitude,
        Day=monthday[1],
        Month=monthday[0],
        Years = weather["Year"],
        Avg_Temp = weather.get("Avg Temp"),
        Max_Wind = weather.get("Max Wind"),
        Precipitation = weather.get("Precipitation"),
        Max_Temp = weather.get("Max Temp"),
        Min_Temp = weather.get("Min Temp")
    )
    session.add(record)

session.commit()
session.close()

