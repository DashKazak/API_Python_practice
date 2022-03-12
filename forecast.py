
import os
import requests
import time
from datetime import datetime
from pprint import pprint
import logging
import requests

#Configuring my logger
logging.basicConfig(filename = 'debug.log', level = logging.DEBUG, format = f'%(asctime)s - %(name)s - %(levelname)s - %(message)s')

url = 'http://api.openweathermap.org/data/2.5/forecast'
key = os.environ.get('weather_key')
#example request



def main():
    location = get_location()
    weather_data, error = get_5day_weather(location,key)
    if error:
        print('Sorry can\'t find weather')
    if weather_data:
        print('forecast run successfully')
        
        
    


def get_location():
    city, country = '',''
    #question about notation above
    while len(city)==0:
        city = input('Enter the name of the city: ').strip()
        if city == '':
            logging.debug(f'The user did not enter city')
    while len(country)!=2 or not country.isalpha():
        country = input('Enter the 2-letter country code: ').strip()
        if country == '':
            logging.debug(f'The user did not enter 2-letter country code')
    location=f'{city},{country}'
    return location


def get_5day_weather(location,key):
    try:
        query={'q':location,'units':'metric', 'appid':key}

        response = requests.get(url,params = query)
        response.raise_for_status() #raise exception for 400 and 500 errors
        data = response.json() #this may error too, if response is not json
        #It currently shows forecast in regards to MN or Central time. I think some users would prefer to see it in the timezone of the location, 
        #I think it's inefficient way but I can't think of any other way:
        #import pytz
        #add as many timezones as possible(there is probably a template)
        #tz_MN = pytz.timezone('America/Chicago)
        #forecast_time = tz_MN

        list_of_forecast = data['list']
        #print(list_of_forecast)
        for forecast in list_of_forecast:
            temp = forecast['main']['temp']
            temp_round = round(temp)
            timestamp=forecast['dt']
            forecast_date = datetime.fromtimestamp(timestamp)
            wind_speed = forecast['wind']['speed']
            description = forecast['weather'][0]['description']
            #print(forecast_time)
            print(f'at {forecast_date} the temperature will be {temp_round}C, the wind speed will be {wind_speed} km/h, can be described as {description}')
        return forecast, None #data is a tuple
    except Exception as e:
        logging.debug(f'Error:', e)
        print(response.text) #added for debugging
        return None, e #tuple will be none


if __name__=='__main__':
    main()