from pkg_resources import UnknownExtra
import requests
from pprint import pprint
import os


#print(key)
url = 'http://api.openweathermap.org/data/2.5/weather'
key=os.environ.get('weather_key')

def main():
    location = get_location()
    weather_data, error = get_current_weather(location,key)
    if error:
        print('Sorry can\'t find weather')
    else:
        current_temp = get_temp(weather_data)
        print(f'The current temperature is {current_temp}C')

def get_location():
    city,country = '',''
    #question about notation aboveM
    while len(city)==0:
        city = input('Enter the name of the city: ').strip()
    while len(country)!=2 or not country.isalpha():
        country = input('Enter the 2-letter country code: ').strip()
    location=f'{city},{country}'
    return location

def get_current_weather(location,key):
    try:
        query={'q':location,'units':'metric', 'appid':key}
        response = requests.get(url,params = query)
        response.raise_for_status() #raise exception for 400 and 500 errors

        data = response.json() #this may error too, if response is not json
        return data, None #data is a tuple
    except Exception as e:
        print(e)
        print(response.text) #added for debugging
        return None, e #tuple will be none

def get_temp(weather_data):
    try:
        temp = weather_data['main']['temp']
        return temp
    except KeyError: 
        print('This data is not in the format expected')
        return 'Unknown'




if __name__=='__main__':
    main()