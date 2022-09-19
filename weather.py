from cmath import e
import os
import requests

api = os.environ['weather_API']
try:
    location = input("Enter city name: ")

    #obtaining lat and long of the city
    #http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}


    generate_api_link = "http://api.openweathermap.org/geo/1.0/direct?q="+location+"&appid="+api
    api_link = requests.get(generate_api_link)
    api_data = api_link.json()
    #print(api_data)
    #obtaining lat and long of the city
    lat = api_data[0]['lat']
    long = api_data[0]['lon']

    # https://api.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid={API key}
    real_api_link = "https://api.openweathermap.org/data/2.5/weather?lat="+str(lat)+"&lon="+str(long)+"&appid="+api
    api_link = requests.get(real_api_link)
    api_data = api_link.json()
    #print(api_data)

    #display
    print("------------Weather details for "+location+"----------")
    print("weather type:", api_data['weather'][0]['description'])
    print("min temp: ", api_data['main']['temp_min']-273)
    print("max temp: ", api_data['main']['temp_max']-273)
    
except:
    print("City name is incorrect!!")
    exit()



