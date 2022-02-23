from http.client import REQUESTED_RANGE_NOT_SATISFIABLE
import os
import requests
from datetime import datetime
from pprint import pprint

key = os.environ.get('weather_key')

query = {'q': 'minneapolis,us', 'units': 'metric', 'appid':key}

url = 'http://api.openweathermap.org/data/2.5/forecast'

#example request

data = requests.get(url,params= query).json()
pprint(data)

list_of_forecast = data['list']

for forecast in list_of_forecast:
    temp = forecast['main']['temp']
    timestamp=forecast['dt']
    forecast_date = datetime.fromtimestamp(timestamp)
    print(f'At {forecast_date} the temperature will be {temp}C')