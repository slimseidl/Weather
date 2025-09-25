Weather History Tracker

A Python project that retrieves, stores, and queries historical daily weather data for a given location. It leverages the Open-Meteo Archive API, Geopy for geocoding, and SQLite (via SQLAlchemy) for persistent storage.

The tool allows you to:

Look up historical weather data (temperature, precipitation, wind speed) for a given date and location across multiple years.

Stores results in a local SQLite database (weather.db).

Prevent duplicate entries using unique constraints.

Query previously stored records and view them in a tabular format.

Features

Fetches daily historical weather records (average, max, and min temperature, wind speed, and precipitation).

Works with either user-provided years or defaults to the last 5 years.

Reverse geocoding to display city/state information.

Stores records in SQLite with SQLAlchemy ORM.

Query tool to retrieve past records by latitude/longitude and date.

Requirements

Python 3.9+ (recommended)

Libraries:

- Requests
- Geopy
- Tabulate
- SQLAlchemy
- See requirements.txt

Usage

Run the script

Input prompts will appear:

Enter City: 
Enter State: 
Enter a month and day in the following format: mm/dd
Enter years to get weather for (space separated), default is last 5:

If no years are provided, the program defaults to the last 5 years.

Example: entering 2019 2020 2021 will pull weather data for that date in those years.

After fetching data:

Records are stored in weather.db.

A summary table is displayed using tabulate.

Example
Enter City:
Chicago
Enter State:
Illinois
Enter a month and day in the following format: mm/dd
07/04
Enter years to get weather for (space separated), default is last 5:

Calling the print_info method: 

Weather information for Chicago, Illinois on July 04 over the last 5 years:
    -Average Temperature: 79.6 degrees Fahrenheit
    -Maximum Temperature: 87.0 degrees Fahrenheit
    -Minimum Temperature: 68.5 degrees Fahrenheit
    -Average Max Wind Speed: 12.40 mph
    -Average Total Precipitation: 0.20"


Database records (queried with query_weather_records):

Month	Day	Year	Average Temp	Max Wind Speed	Total Precipitation	Max Temp	Min Temp	City	State
7	4	2019	77.1	11.0	0.10	86.0	68.0	Chicago	Illinois
7	4	2020	80.2	13.5	0.30	88.0	69.0	Chicago	Illinois
File Overview

Weather.py → Defines the WeatherData class (fetching and aggregating weather data).

weather_app.py → Main entry script; handles input, database interaction, and queries.

weather.db → Auto-created SQLite database storing historical records.

Roadmap / Possible Improvements:

Add CLI arguments to bypass input().

Include data visualization (e.g., matplotlib plots for temperature trends).

Expand support for multiple locations at once.

Export query results to CSV.

License:

Powered by open-meteo