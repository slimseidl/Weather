from geopy.geocoders import Nominatim
import requests
from Weather import WeatherData
from sqlalchemy import create_engine, Integer, Float, Column, String, UniqueConstraint
from sqlalchemy.orm import declarative_base, sessionmaker
from tabulate import tabulate
import sqlite3
from sqlalchemy.exc import IntegrityError


geolocator = Nominatim(user_agent="weather_app")


city = input(f'Enter City: \n')
state = input(f'Enter State: \n')
try:
    location = geolocator.geocode(f'{city}, {state}',timeout=30)
except Exception as e:
    print("Geocoding failed:", e)
    location = None
latitude = location.latitude
longitude = location.longitude
monthday = input("Enter a month and day in the following format: mm/dd\n").split("/")
# years = input().split() default is previous 5 years? 

WeatherForLocation = WeatherData(latitude, longitude, monthday[0], monthday[1])
weather_data = WeatherForLocation.get_weather()


base = declarative_base()


class WeatherRecords(base):
    __tablename__ = "HistoricalWeatherRecords"
    id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    month = Column(Integer,nullable=False)
    day = Column(Integer,nullable=False)
    years = Column(Integer,nullable=False)
    avg_temp = Column(Float)
    max_wind = Column(Float)
    precipitation = Column(Float)
    max_temp = Column(Float)
    min_temp = Column(Float)
    city = Column(String, nullable=True)
    state = Column(String, nullable=True)

    __table_args__ = (
        UniqueConstraint('latitude', 'longitude', 'month', 'day', 'years', name='uq_weather_record'),
    )


engine = create_engine('sqlite:///weather.db')
base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

for weather in weather_data:
    record = WeatherRecords(
        latitude=latitude,
        longitude=longitude,
        day=monthday[1],
        month=monthday[0],
        years = weather["Year"],
        avg_temp = weather.get("Avg Temp"),
        max_wind = weather.get("Max Wind"),
        precipitation = weather.get("Precipitation"),
        max_temp = weather.get("Max Temp"),
        min_temp = weather.get("Min Temp"),
        city = city,
        state = state
    )
    try:
        session.add(record)
        session.commit()
    except IntegrityError:
        session.rollback()
        print("Duplicate record skipped.")

session.close()

def query_weather_records(latitude, longitude, month,day):
    conn = sqlite3.connect("weather.db")

    cursor = conn.cursor()

    query = """SELECT * 
               FROM HistoricalWeatherRecords"""
    
        # WHERE latitude = ? and longitude = ?
        #         and month = ? and day = ?

    cursor.execute(query) # , (latitude, longitude, month, day)

    results = cursor.fetchall()


    results_list = []
    for result in results:

        data = {
            "Month": result[3],
            "Day": result[4],
            "Year": result[5],
            "Average Temp": result[6],
            "Max Wind Speed": result[7],
            "Total Precipitation": result[8],
            "Max Temp": result[9],
            "Min Temp": result[10],
            "City": result[11],
            "State": result[12]
        }

        results_list.append(data)

    print(tabulate(results_list,headers="keys"))
    conn.close()

query_weather_records(latitude,longitude,monthday[0], monthday[1])